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

    pid_t p, done_p;
    p = 0;

    p = fork();

    if(p == 0) {
        cout << "eu sou filho " << commands[0].args()[0] << endl;
        execlp(commands[0].filename(), commands[0].filename(), commands[0].argv()[1], NULL);

    } else {
        wait(0);
        cout << "voltando pro terminal" << endl;
    }

    return 0;
}