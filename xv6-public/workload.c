#include "types.h"
#include "user.h"

int 
fact(int n)
{
    printf(1, "\n Value is %d\n", n);

    if(n == 1) return 1;
    else return n * fact(n - 1);
}

void 
up(int n){
    int i = 0;
    while(i++ < n);
}

int 
main()
{
    for (int i = 0; i < 10; i++) {

        if (fork() == 0) {
            int pid = getpid();
            setpriority(pid, pid % 4);
            printf(1, "\n PRIORITY %d of %d\n", getpriority(pid), pid);
            up(1000);
            exit();
        
        } else {
            for(int j = 0; j < 20; j++) wait();
        }
    }

    return 0;
}
