#include "types.h"
#include "stat.h"
#include "user.h"
#include "fcntl.h"

int main(int argc, char *argv[])
{
    int value, pid;

    if (argc < 2 || argc > 3)
    {
        printf(2, "Usage: nice [pid] # To get process priority.\n       nice [pid] [priority] # To set process priority.\n" );
        exit();
    }

    pid = atoi(argv[1]);

    if (argc == 3)
    {
        value = atoi(argv[2]);

        if (value < 0 || value > 3)
        {
            printf(2, "Invalid priority (0-3)! # 0 is the highest priority\n" );
            exit();
        }

        setpriority(pid, value);

    } else printf(1, "%d\n", getpriority(pid));

    exit();
}