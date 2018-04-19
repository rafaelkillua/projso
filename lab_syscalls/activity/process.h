#include "../xeu_utils/StreamParser.h"
#include "sys/types.h"
#include "unistd.h"
#include "stdlib.h"
#include "sys/wait.h"

#include <iostream>
#include <vector>

using namespace xeu_utils;
using namespace std;

void left_child(int pp[2], int j) {
    
    close(pp[0]);
    dup2(j, 0);
    dup2(pp[1], 1);

}

int right_child(int pp[2]) {

    //close(pp[1]);
    dup2(pp[0], 0);
    dup2(pp[1], 1);
    return dup(pp[1]);
}

int process(const vector<Command>& commands) {

    int i, j = 0, pp[2];
    int n = commands.size();
    
    for(i = 0; i < n - 1; i = i + 2) {

        pipe(pp);
        pp[0] = j;

        if (fork() == 0) {

            left_child(pp, j);
            execvp(commands[i].filename(), commands[i].argv());

        }

        if (n - i >= 2 && fork() == 0) {

            j = right_child(pp);
            cout << "UÉ meio " << j << endl;
            execvp(commands[i + 1].filename(), commands[i + 1].argv());

        }

    }

    close(pp[0]);
    close(pp[1]);
    cout << "UE final " << j << endl;
    dup2(1, j);
    wait(0);

    return 0;
}