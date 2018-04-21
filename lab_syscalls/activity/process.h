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

    int n = commands.size();
    int i, pp[n][2];

    if(n > 1) { for(i = 0; i < n - 1; i ++) {
        pipe(pp[i]);
        cout << pp[i][0] << " " << pp[i][1] << endl;
        } 
    }    

    for(i = 0; i < n; i++) {

        if (fork() == 0) {
        
            if(n > 1) {
                
                if(i == 0){ 
                    cout << "primeiro "<< pp[i][1] << endl;
                    dup2(pp[i][1], 1); 

                } else if (i < n - 1) { 
                    cout << "meio entrada: " << pp[i-1][0] << " saida: " << pp[i][1] << endl;
                    dup2(pp[i-1][0], 0);
                    dup2(pp[i][1], 1); 

               } else {
                    cout << "ultimo " << pp[i-1][0] << endl;
                    dup2(pp[i-1][0], 0);
                }                
            }

            execvp(commands[i].filename(), commands[i].argv());
        }        
    }

    if(n > 1){
        for(i = 0; i < n - 1; i ++) {
            close(pp[i][0]);
            close(pp[i][1]);
        }
    }

    wait(0);
    return 0;
}