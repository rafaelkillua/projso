#include "../xeu_utils/StreamParser.h"
#include "sys/types.h"
#include "unistd.h"
#include "stdlib.h"
#include "sys/wait.h"
#include "sys/types.h"
#include "sys/stat.h"
#include "fcntl.h"

#include <iostream>
#include <vector>

using namespace xeu_utils;
using namespace std;

void conf_file_fd(const Command command){

    for (size_t j = 0; j < command.io().size(); j++) {
        
        IOFile io = command.io()[j];
        int fd;

        if (io.is_input()) {
        
            int fdin = open(io.path().c_str(), O_RDONLY);
            
            if(io.has_fd())
                fd = io.fd();
            else
                fd = 0;

            dup2(fdin, fd);
        
        } else if (io.is_output()) {
        
            int fdout = open(io.path().c_str(), O_WRONLY|O_CREAT, 0666);

            if(io.has_fd())
                fd = io.fd();
            else
                fd = 1;

            dup2(fdout, fd);
        }
    }
}

int process(const vector<Command>& commands) {

    int n = commands.size();
    int i, pp[n][2];

    if (n > 1) {
        
        for (i = 0; i < n - 1; i ++) 
            pipe(pp[i]);
    
    }

    for (i = 0; i < n; i++) {

        if (fork() == 0) {

            if (n > 1) {

                if(i < n - 1) {

                    conf_file_fd(commands[i]);
                    close(pp[i][0]);
                    dup2(pp[i][1], 1);
                }

                if(i > 0) {

                    conf_file_fd(commands[i]);
                    close(pp[i-1][1]);
                    dup2(pp[i-1][0], 0);                    
                }
            }

            conf_file_fd(commands[i]);
            execvp(commands[i].filename(), commands[i].argv());

        } else {

            close(pp[i][1]);
            wait(0);
        }
    }

    return 0;
}