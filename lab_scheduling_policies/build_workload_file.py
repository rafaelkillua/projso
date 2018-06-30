from random import randint
import ConfigParser

def build_process_file():

    configParser = ConfigParser.RawConfigParser()
    path = "sim.conf"
    configParser.read(path)
    output = configParser.get("build", "workload_path")
    number_of_process = configParser.getint("build", "number_of_process")
    
    f = open(output, 'a')
    timestamp_c = 1
    pid_c = 1

    for i in xrange(number_of_process):
        priority = randint(1, 20)
        service_time = 100
        f.write(
            str(timestamp_c) + ' ' +
            str(pid_c) + ' ' +
            str(priority) + ' ' +
            str(service_time) + '\n'
        )
        timestamp_c += randint(1, 50)
        pid_c += 1

    f.close()

if __name__ == '__main__':
    build_process_file()
