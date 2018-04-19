#include "../xeu_utils/StreamParser.h"
#include "sys/types.h"
#include "unistd.h"
#include "stdlib.h"
#include "sys/wait.h"

#include <iostream>
#include <vector>

using namespace xeu_utils;
using namespace std;

void left_child(Command command, int pp[2]) {
    
    close(pp[0]);
    dup2(pp[1], 1);
    execvp(command.filename(), command.argv());

}

void right_child(Command command, int pp[2]) {

    close(pp[1]);
    dup2(pp[0], 0);
    execvp(command.filename(), command.argv());

}

int process(const vector<Command>& commands) {

    int i, pp[2];    
    int n = commands.size();

    pipe(pp);

    if (fork() == 0) {

        left_child(commands[0], pp);

    }

    if (fork() == 0) {

        right_child(commands[1], pp);

    }

    close(pp[0]);
    close(pp[1]);
    wait(0);

    return 0;
}