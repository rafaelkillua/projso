# Generate timeline plot.
# This plot shows the progress of each process over the time.
# The history of a process is divided in two moments: expected time and extra time.
# The expected time is the time that the process needs to terminate its job.
# The extra time is the additional time that the processes needed to terminate its job.

library(timelineS)
setwd("~/Documents/workspace/projso/lab_scheduling_policies")

#Round Robin
timeline <- read.table("output/time_line20_rr.ffd", header = T, sep = " ")

png(filename = "plots/timeline20_rr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Priority Random
timeline <- read.table("output/time_line20_pr.ffd", header = T, sep = " ")

png(filename = "plots/timeline20_pr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Xv6
timeline <- read.table("output/time_line20_xv6.ffd", header = T, sep = " ")

png(filename = "plots/timeline20_xv6_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Kernel
timeline <- read.table("output/time_line20_kr.ffd", header = T, sep = " ")

png(filename = "plots/timeline20_kr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()