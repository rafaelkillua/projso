import sys
from sys import stderr
from process import Process
from sched_policy import Scheduler
from sim_engine import Event
from sim_engine import EventStream
import uuid
from datetime import datetime
import ConfigParser

import priority_random as priority_random


class WorkloadParser(object):
    def parse(self, filename):
        file_lines = []
        try:
            with open(filename, 'r') as wk_load_file:
                file_lines = wk_load_file.readlines()
        except IOError:
            stderr.write('Unable to read workload file!\n')
        proc_list = []
        for line in file_lines:
            timestamp, pid, priority, service_t = map(int, line.split())
            proc_list.append(Process(timestamp, pid, priority, service_t))
        return proc_list

def run_simulation(event_stream):

    class Clock:
        current_time = 0
        @classmethod
        def now(cls):
            return Clock.current_time

    class ProcTable:
        def __init__(self):
            self.procs = {}
        def add(self, proc):
            self.procs[proc.get_pid()] = proc
        def remove(self, proc):
            self.procs.pop(proc.get_pid(), None)
        def size(self):
            return len(self.procs)

    class CPU:
        def __init__(self):
            self.running_proc = None
        def take_cpu(self):
            taken = self.running_proc
            if taken:
                assert taken.get_state() == Process.RUNNING
                taken.set_state(Process.RUNNABLE)
            self.running_proc = None
            return taken
        def enter_cpu(self, process):
            assert process.get_state() == Process.RUNNABLE
            self.running_proc = process
            self.running_proc.set_state(Process.RUNNING)

    def update_usage_t(proc, usage_interval):
        previous_usage_t = proc.get_usage_t()
        proc.set_usage_t(previous_usage_t + usage_interval)

    def process_is_done(proc):
        return proc.get_service_t() <= proc.get_usage_t()

    #init main loop
    cpu = CPU()
    scheduler = select_scheduler()
    p_table = ProcTable()

    #procs seen during simulation, to generate output
    procs = []

    while True:
        event = event_stream.next()
        if (not event): break

        previous_t = Clock.current_time
        Clock.current_time = event.get_timestamp()
        schedule_timestamp = Clock.now() + SLICE_DURATION

        if (event.get_type() == event_types.SCHEDULE):

            #remove old runnning proc
            out_proc = cpu.take_cpu()
            out_pid = None

            #update out proc stats
            if (out_proc):
                update_usage_t(out_proc, Clock.now() - previous_t)
                out_pid = out_proc.get_pid()

            #choose the next proc to enter cpu
            in_proc = scheduler.schedule(out_pid, Clock.now() - previous_t)

            if in_proc and in_proc.get_creation_t() == -1:
                in_proc.set_creation_t(Clock.now())

            #enter cpu and schedule an exit event, if necessary
            if (in_proc):
                cpu.enter_cpu(in_proc)
                remaining_t = in_proc.get_service_t() - in_proc.get_usage_t()
                if (remaining_t < SLICE_DURATION and remaining_t >= 0):
					exit_timestamp = Clock.now() + remaining_t
					if (remaining_t == 0):
						exit_timestamp += 1
					event_stream.add(Event(event_types.EXIT_PROC, exit_timestamp, in_proc))
                else:
					event_stream.add(Event(event_types.SCHEDULE, schedule_timestamp, None))
            elif (p_table.size() > 0):
				event_stream.add(Event(event_types.SCHEDULE, schedule_timestamp, None))
				

        elif (event.get_type() == event_types.ALLOC_PROC):

            new_proc = event.get_context()

            #update simulation stats
            p_table.add(new_proc)
            scheduler.alloc_proc(new_proc, Clock.now() - previous_t)
            procs.append(new_proc)
            
            if (p_table.size() == 1):
				event_stream.add(Event(event_types.SCHEDULE, schedule_timestamp, None))				

        elif (event.get_type() == event_types.EXIT_PROC):

            exit_proc = event.get_context()

            #remove from cpu
            cpu.take_cpu()

            update_usage_t(exit_proc, Clock.now() - previous_t)
            if process_is_done(exit_proc):
                exit_proc.set_state(Process.TERMINATED)

            #update simulation stats
            exit_proc.set_exit_t(Clock.now())

            #clean state
            exit_pid = exit_proc.get_pid()
            scheduler.exit(exit_pid)
            p_table.remove(exit_proc)

            #force a new proc to enter the cpu
            event_stream.add(Event(event_types.SCHEDULE, Clock.now() + 1, None))

    return procs

def enum(**enums):
    return type('Enum', (), enums)
event_types = enum(ALLOC_PROC=1, EXIT_PROC=2, SCHEDULE=3)

SLICE_DURATION = 20

def generate_output(out):
    # Generate output file.

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    extra_time_output = configParser.get("simulation", "extra_time_path")

    try:
        with open(extra_time_output, 'a') as extra_time_file,\
            open(extra_time_output, 'r') as extra_time_file_r:
            
            if extra_time_file_r.read() == "":
                extra_time_file.write("process extra_time wait_time priority\n")

            for proc in out:

                print "Priority ", proc.get_priority(), priority_random.find_priority(proc.get_priority())
                expect_exit_t = proc.get_timestamp() + proc.get_service_t()
                extra_t = proc.get_exit_t() - expect_exit_t
                wait_time = proc.get_creation_t() - proc.get_timestamp()

                extra_time_file.write(str(proc.get_pid()) + " " + str(extra_t) + " " +\
                                    str(wait_time) + " " +\
                                    str(priority_random.find_priority(proc.get_priority())) +'\n')
            
    except Exception as e:
        print 'Unable to write file property: %s.' % str(e)

def select_scheduler():

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    algorithm = configParser.get("simulation", "scheduler_algorithm")

    try:
        return getattr(priority_random, algorithm)()

    except AttributeError as err:
        print err.message
        return Scheduler()

if __name__ == '__main__':
    #read workload file in the standard directory
    wlp = WorkloadParser()

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    input_file = configParser.get("simulation", "workload_path")

    ordered_process_list = wlp.parse(input_file)
    events = [Event(event_types.ALLOC_PROC, proc.get_timestamp(), proc)
                for proc in ordered_process_list]

    #add an schedule event to proper fire the engine
    events.insert(0, Event(event_types.SCHEDULE, 0, None))
    e_stream = EventStream(events)

    #fire
    output = run_simulation(e_stream)
    generate_output(output)
