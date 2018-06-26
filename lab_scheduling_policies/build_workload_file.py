from random import randint
import ConfigParser

def build_process_file():

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    output = configParser.get("workload", "path")
    
    f = open(output, 'w')
    proc_list = []
    timestamp_c = 1
    pid_c = 1

    for i in xrange(30):
        priority = randint(1, 20)
        service_time = 40
        proc_list.append(
            str(timestamp_c) + ' ' +
            str(pid_c) + ' ' +
            str(priority) + ' ' +
            str(service_time) + '\n'
        )
        timestamp_c += randint(1, 50)
        pid_c += 1

    f.writelines(proc_list)
    f.close()

if __name__ == '__main__':
    build_process_file()
