from random import randint
import ConfigParser

def build_process_file():

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    output = configParser.get("build", "workload_path")
    number_of_process = configParser.getint("build", "number_of_process")
    
    f = open(output, 'w')
    timestamp_c = 1
    pid_c = 1

    for i in xrange(number_of_process):
        priority = set_priority(i % 4)
        service_time = 100
        f.write(
            str(timestamp_c) + ' ' +
            str(pid_c) + ' ' +
            str(priority) + ' ' +
            str(service_time) + '\n'
        )
        timestamp_c = 1
        pid_c += 1

    f.close()

def set_priority(value):
    if value == 0: return 5
    elif value == 1: return 10
    elif value == 2: return 15
    else: return 20

if __name__ == '__main__':
    build_process_file()
