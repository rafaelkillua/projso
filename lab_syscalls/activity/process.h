#include "../xeu_utils/StreamParser.h"
#include "sys/types.h"
#include "unistd.h"
#include "stdlib.h"
#include "sys/wait.h"

#include <iostream>
#include <vector>

using namespace xeu_utils;
using namespace std;

int process(const vector<Command>& commands) {

    int i, pp[2];
    pid_t pid = 0;
    
    int n = commands.size();

    for(i = 0; i < n; i++) {
        
        if(i == 0) {
            pipe(pp);
        }

        pid = fork();

        if(pid == 0) { 
            if(n > 1) {
                
                if(i == 0) {
                
                    close(1);
                    close(pp[0]);
                    dup2(pp[1], 1);
                
                } else if(i == n - 1) {
                
                    close(0);
                    close(pp[1]);
                    dup2(pp[0], 0);                
                
                } else {

                    close(1);
                    close(pp[0]);
                    dup2(pp[1], 1);

                    pipe(pp);                

                    close(0);
                    close(pp[1]);
                    dup2(pp[0], 0);                    
                }
            }

            execvp(commands[i].filename(), commands[i].argv());    
        } 
    }

    if(pid != 0) {        
        if(n > 1) {
            close(pp[0]);
            close(pp[1]);    
        }
        wait(0);
    }

    return 0;
}