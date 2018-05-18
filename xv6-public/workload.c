#include "types.h"
#include "user.h"
#include "fcntl.h"

unsigned long long 
fibo(unsigned long long n)
{
    if(n == 0 || n == 1) return 1;
    else return fibo(n -1) + fibo(n - 2);
}

int 
main()
{

    int pid = getpid();
    setpriority(pid, 3);

    for (int i = 0; i < 50; i++) {

        if (fork() == 0) {

            int pid = getpid();
            setpriority(pid, pid % 4);
            printf(1, "\nSTARTED %d of %d\n", pid, getpriority(pid));
            fibo(30);
            printf(1, "\nFINISHED %d of %d\n", pid, getpriority(pid));
            exit();
        
        } else {
        }
    }

    for(int j = 0; j < 50; j++) wait();
    return 0;
}
