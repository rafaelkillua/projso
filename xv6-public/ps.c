#include "types.h"
#include "user.h"
#include "ps.h"

int 
main(int argc, char *argv[])
{
	static int MAX = 20;
	struct uproc tbl[MAX];
	
	int size = getprocs(MAX, tbl);
	
	if(size == 0)
	{
		printf(2, "uproc_failed: get table for uproc failed\n");
	    exit();
    }
	
	printf(1,"PID    PPID    PR    STATE        NAME\n");

	int i;
	for (i=0; i < size;i++){
		printf(1,"%d      %d       %d     %s     %s\n",
		tbl[i].pid, tbl[i].ppid, tbl[i].priority, tbl[i].state, tbl[i].name);
	}
	
   exit();
}