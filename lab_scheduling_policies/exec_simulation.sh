#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
for i in $(seq 1 5) 
do 
	python sched_simulator.py
done
