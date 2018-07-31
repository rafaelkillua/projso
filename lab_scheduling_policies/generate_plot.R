# library
library(timelineS)
library(ggplot2)
# library(magrittr)
# library(ggpubr)
setwd("~/Documents/workspace/projso/lab_scheduling_policies")
# Generate timeline plot.
# This plot shows the progress of each process over the time.
# The history of a process is divided in two moments: expected time and extra time.
# The expected time is the time that the process needs to terminate its job.
# The extra time is the additional time that the processes needed to terminate its job.

raw_data <- read.table("output/time_line_rnd_rr.ffd", header = T, sep = " ")

png(filename = "plots/timeline_rnd_rr_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = raw_data, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

# Generate boxplot.
# BoxPlot about the extra time needed by the processes.

extra_time_data = read.table("output/extra_time_busy_xpr.ffd", header = T)

png(filename = "plots/extra_time_busy_xpr_plot.png", width = 600, height = 600, units = "px",res = 120)
ggplot(data = extra_time_data, aes(y = extra_time_data$extra_time, x = extra_time_data$priority, group = extra_time_data$priority)) +
  geom_boxplot() +
  labs(title = "Extra time Execution", x = "Priority", y = "Extra Time In System")
dev.off()

workload_data = read.table("input/workload_busy.ffd", header = F)
workload_data$V5 <- ifelse(workload_data$V3 <= 5, 0,
                          ifelse(workload_data$V3 <= 10, 1,
                                 ifelse(workload_data$V3 <= 15, 2, 3)
                                 )
                          )

png(filename = "plots/workload_busy_plot.png", width = 600, height = 600, units = "px",res = 120)
ggplot(data = workload_data, aes(y = (workload_data$V4 + workload_data$V1), x = workload_data$V5, group = workload_data$V5)) +
  geom_boxplot() +
  labs(title = "Workload", x = "Priority", y = "Expected Time In System")
dev.off()
