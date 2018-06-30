from random import randint
from process import Process

class RoundRobin:

	def __init__(self):
		self._process_list = []
		self._last_index = 0

	def alloc_proc(self, process, delta_t):
		"""Update the data structures to recognize a new process was created"""
		print "Allocating process ", process.get_pid()
		self._process_list.append(process)

	def schedule(self, pid, delta_t):
		"""Return the next process to run in the cpu.

		out_process_pid -- the pid of the process that just left the cpu, or None
		in case there was no process running. The engine is responsible
		for updating the usage time.
		"""
		size = len(self._process_list)

		if size == 0: 
			return None

		process = self._process_list[self._last_index % size]
		self._last_index = self._last_index + 1
		return process

	def exit(self, process_pid):
		"Update data structures to reconize a process was finished"
		# print "Removing process ", process_pid
		self._process_list = [proc for proc in self._process_list if proc.pid != process_pid]

class PriorityRandom(RoundRobin):
	"""Implements xv6 scheduler without bugs"""

	def __init__(self):
		RoundRobin.__init__(self)

	def schedule(self, pid, delta_t):
		"""Return the next process to run in the cpu.

		out_process_pid -- the pid of the process that just left the cpu, or None
		in case there was no process running. The engine is responsible
		for updating the usage time.
		"""
		if len(self._process_list) == 0:
			return None

		if self._last_index >= len(self._process_list):
			self._last_index = 0
		
		while True:

			priority = sort_priority()
			# print "SCHEDULING PRIORITY ", priority, "\n"
			actual_index = self._last_index + 1

			while True:
				
				if actual_index >= len(self._process_list):
					actual_index = 0
				
				process =  self._process_list[actual_index]       
				
				if find_priority(process.get_priority()) == priority:
					self._last_index = self._process_list.index(process)
					# print "FIND PROCESS " , actual_index, "\n"
					return process
								
				else:
					actual_index += 1

					if actual_index >= len(self._process_list):
						actual_index = 0

					# print "LAST INDEX: ", self._last_index, " ACTUAL INDEX: ", actual_index					

					if actual_index == self._last_index: 
						break

class Xv6PriorityRandom(RoundRobin):
	"""Implements xv6 scheduler with bugs"""

	def __init__(self):
		RoundRobin.__init__(self)

	def schedule(self, pid, delta_t):
		"""Return the next process to run in the cpu.

		out_process_pid -- the pid of the process that just left the cpu, or None
		in case there was no process running. The engine is responsible
		for updating the usage time.
		"""

		if len(self._process_list) == 0: 
			return None

		if self._last_index >= len(self._process_list):
			self._last_index = 0
		
		while True:

			priority = sort_priority()
			# print "SCHEDULING PRIORITY ", priority, "\n"
			actual_index = self._last_index + 1

			while True:
				# print "FIND PROCESS " , actual_index, "\n"
				
				if actual_index >= len(self._process_list):
					actual_index = 0
				
				process =  self._process_list[actual_index]       
				
				if find_priority(process.get_priority()) == priority:
					self._last_index = self._process_list.index(process)
					return process
								
				else:
					actual_index += 1

					if actual_index >= len(self._process_list):
						actual_index = 0
						priority = sort_priority()

					# print "LAST INDEX: ", self._last_index, " ACTUAL INDEX: ", actual_index					

					if actual_index == self._last_index: 
						break


def find_priority(value):

	if value <= 5: return 0
	elif value <= 10: return 1
	elif value <= 15: return 2
	else: return 3

def sort_priority():
	
	rand = randint(1, 100)

	if rand <= 50: return 3
	elif rand <= 75: return 2
	elif rand <= 90: return 1
	else: return 0

if __name__ == '__main__':

    sched = Xv6PriorityRandom()

    timestamp_c = 0
    pid_c = 0

    for i in xrange(30):
        timestamp_c += randint(1, 50)
        pid_c += 1
        priority = randint(0, 20)
        service_time = randint(40, 400)

        process = Process(timestamp_c, pid_c, priority, service_time)
        sched.alloc_proc(process.get_pid(), 0)
    
    print sched._process_list
    print "\n"
    
    i = 0
    while i < 20:
        process = sched.schedule(0)
        sched._process_list.remove(process)
        print process
        print "\n"
        i += 1
