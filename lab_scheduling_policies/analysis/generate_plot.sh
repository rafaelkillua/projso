#!/bin/bash

echo "Start plot"
Rscript workload_plot.R
Rscript timeline_plot.R
Rscript extratime_plot.R
echo "Finish plot"
