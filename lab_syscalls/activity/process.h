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

    pid_t p = 0;
    int i;

    for(i = 0; i < commands.size(); i++) {

        p = fork();

        if(p == 0) {
            cout << "eu sou filho " << i << commands[i].args()[0] << endl;
            execvp(commands[i].filename(), commands[i].argv());
        
        } 
    }

    if(p != 0) {
        wait(0);
        cout << "voltando pro terminal after " << i << endl;
    }

    return 0;
}