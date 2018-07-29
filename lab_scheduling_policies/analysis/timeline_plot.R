# Generate timeline plot.
# This plot shows the progress of each process over the time.
# The history of a process is divided in two moments: expected time and extra time.
# The expected time is the time that the process needs to terminate its job.
# The extra time is the additional time that the processes needed to terminate its job.

library(timelineS)
setwd("~/Documents/workspace/projso/lab_scheduling_policies")

# 40 Processos

#Round Robin
timeline <- read.table("output/time_line40_rr.ffd", header = T, sep = " ")

png(filename = "plots/timeline40_rr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Priority Random
timeline <- read.table("output/time_line40_pr.ffd", header = T, sep = " ")

png(filename = "plots/timeline40_pr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Xv6
timeline <- read.table("output/time_line40_xv6.ffd", header = T, sep = " ")

png(filename = "plots/timeline40_xv6_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Kernel
timeline <- read.table("output/time_line40_kr.ffd", header = T, sep = " ")

png(filename = "plots/timeline40_kr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

# 400 Processos

#Round Robin
timeline <- read.table("output/time_line400_rr.ffd", header = T, sep = " ")

png(filename = "plots/timeline400_rr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Priority Random
timeline <- read.table("output/time_line400_pr.ffd", header = T, sep = " ")

png(filename = "plots/timeline400_pr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Xv6
timeline <- read.table("output/time_line400_xv6.ffd", header = T, sep = " ")

png(filename = "plots/timeline400_xv6_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Kernel
timeline <- read.table("output/time_line400_kr.ffd", header = T, sep = " ")

png(filename = "plots/timeline400_kr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

# 4000 Processos

#Round Robin
timeline <- read.table("output/time_line4000_rr.ffd", header = T, sep = " ")

png(filename = "plots/timeline4000_rr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Priority Random
timeline <- read.table("output/time_line4000_pr.ffd", header = T, sep = " ")

png(filename = "plots/timeline4000_pr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Xv6
timeline <- read.table("output/time_line4000_xv6.ffd", header = T, sep = " ")

png(filename = "plots/timeline4000_xv6_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

#Kernel
timeline <- read.table("output/time_line4000_kr.ffd", header = T, sep = " ")

png(filename = "plots/timeline4000_kr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = timeline, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()