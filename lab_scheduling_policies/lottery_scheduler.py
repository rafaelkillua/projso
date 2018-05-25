from random import randint
from process import Process

class LotteryScheduler():

    def __init__(self):
        self._process_list = []
        self._last_index = 0

    def alloc_process(self, process):
        self._process_list.append(process)


    def scheduler(self, pid):

        while True:
            print "SCHEDULING\n"
            priority = self._select_priority()
            actual_index = self._last_index + 1

            while True:
                print "FIND PROCESS " , actual_index, "\n"
                
                if actual_index >= len(self._process_list):
                    actual_index = 0
                
                process =  self._process_list[actual_index]       
                
                if self._find_priority(process.get_priority()) == priority:
                    self._last_index = self._process_list.index(process)
                    return process
                                
                else:
                    actual_index += 1
                    
                    if actual_index == self._last_index: 
                        break


    def _find_priority(self, value):

        if value <= 10: return 3
        elif value <= 20: return 2
        elif value <= 30: return 1
        else: return 0

    def _select_priority(self):
        
        rand = randint(1, 100)

        if rand <= 50: return 3
        elif rand <= 75: return 2
        elif rand <= 90: return 1
        else: return 0

if __name__ == '__main__':

    sched = LotteryScheduler()

    timestamp_c = 0
    pid_c = 0

    for i in xrange(30):
        timestamp_c += randint(1, 50)
        pid_c += 1
        priority = randint(0, 20)
        service_time = randint(40, 400)

        process = Process(timestamp_c, pid_c, priority, service_time)
        sched.alloc_process(process)
    
    print sched._process_list
    print "\n"
    
    i = 0
    while i < 20:
        process = sched.scheduler(0)
        sched._process_list.remove(process)
        print process
        print "\n"
        i += 1