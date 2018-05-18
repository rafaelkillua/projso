#include "types.h"

struct uproc {
    int pid;
  	uint ppid;
		int priority;
		char state[10];
		char name[16];
};
