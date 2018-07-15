from process import Process
from params_py import PRIORITY_ONE, PRIORITY_TWO, PRIORITY_THREE, PRIORITY_FOUR 

class Scheduler:
	def __init__(self):
		"""Data structure which contains all processes"""
		self.processes = []
		self.last_proc_prio_two = None
		self.last_proc_prio_three = None
		self.last_proc_prio_four = None

	def schedule(self, out_process_pid, delta_t):
		"""Return the next process to run in the cpu.
		out_process_pid -- the pid of the process that just left the cpu, or None
		in case there was no process running. The engine is responsible
		for updating the usage time.
		"""
		self._avoid_starvation()

		proc_to_run = self._next_proc(out_process_pid, PRIORITY_ONE)
		
		if (proc_to_run):
			proc_to_run.change_current_to_real_priority()
			return proc_to_run
		else:
			proc_to_run = self._next_proc(self.last_proc_prio_two, PRIORITY_TWO)
			
			if (proc_to_run):
				proc_to_run.change_current_to_real_priority()
				self.last_proc_prio_two = proc_to_run.get_pid()
				return proc_to_run
			else:
				proc_to_run = self._next_proc(self.last_proc_prio_three, PRIORITY_THREE)
			
				if (proc_to_run):
					proc_to_run.change_current_to_real_priority()
					self.last_proc_prio_three = proc_to_run.get_pid()
					return proc_to_run
				else:
					proc_to_run = self._next_proc(self.last_proc_prio_four, PRIORITY_FOUR)
					
					if (proc_to_run):
						proc_to_run.change_current_to_real_priority()
						self.last_proc_prio_four = proc_to_run.get_pid()
						return proc_to_run
					else:
						return None
	
	def alloc_proc(self, process, delta_t):
		"""Update the data structures to recognize a new process was created"""
		self.processes.append(process)

	def _next_proc(self, last_proc_pid, priority_interval):
		"""Gets the next runnable process in priority interval"""
		proc = None
		
		if (len(self.processes) > 0):
			for i in range(len(self.processes)):
				if (self.processes[i].get_pid() == last_proc_pid):
					break
			
			if ((i + 1) == len(self.processes)):
				index = 0
			else:
				index = i + 1	
			
			while (index != i):
				if (self.processes[index].get_current_priority() in priority_interval):
					break
					
				index += 1
				
				if (index == len(self.processes)):
					index = 0
			
			if (self.processes[index].get_current_priority() in priority_interval):
				proc = self.processes[index]
						
		return proc

	def _avoid_starvation(self):
		"""Decrements current priority to avoid starvation"""
		proc_prio_two = self._next_proc(self.last_proc_prio_two, PRIORITY_TWO)

		if proc_prio_two:
			proc_prio_two.decrement_current_priority()

		proc_prio_three = self._next_proc(self.last_proc_prio_three, PRIORITY_THREE)
	
		if proc_prio_three:
			proc_prio_three.decrement_current_priority()

		proc_prio_four = self._next_proc(self.last_proc_prio_four, PRIORITY_FOUR)

		if proc_prio_four:
			proc_prio_four.decrement_current_priority()

	def exit(self, process_pid):
		"""Removes a process from process list"""
		for i in range(len(self.processes)):
			if self.processes[i].get_pid() == process_pid:
				del self.processes[i]
				break