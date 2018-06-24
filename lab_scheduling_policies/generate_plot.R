# library
library(timelineS)
setwd("~/Documents/workspace/projso/lab_scheduling_policies")
# Generate timeline plot.
# This plot shows the progress of each process over the time.
# The history of a process is divided in two moments: expected time and extra time.
# The expected time is the time that the process needs to terminate its job.
# The extra time is the additional time that the processes needed to terminate its job.

raw_data <- read.table("timeline-output.ffd", header = T, sep = " ")

png(filename = "timeline_plot.png", width = 1000, height = 600, units = "px",res = 120)
timelineG(df = raw_data, names = "process", phase = "service", start = "start_t", end = "end_t")
dev.off()

# Generate boxplot.
# BoxPlot about the extra time needed by the processes.

extra_time_data = read.table("2018-06-24 02:07:19.720020extra-time-output.ffd", header = F)

png(filename = "extra_time_plot.png", width = 600, height = 600, units = "px",res = 120)
boxplot(x = extra_time_data$V1, ylab = "Extra processing time")
dev.off()

png(filename = "test_plot.png", width = 600, height = 600, units = "px",res = 120)
ggplot2::ggplot(data = extra_time_data, ggplot2::aes(y = extra_time_data$V1, x = extra_time_data$V2, group = extra_time_data$V2)) + ggplot2::geom_boxplot()
dev.off()


#list all csv files from the current directory
list.files(pattern="output.ffd$") # use the pattern argument to define a common pattern  for import files with regex. Here: .csv

# create a list from these files
list.filenames<-list.files(pattern="output.ffd$")
list.filenames

# create an empty list that will serve as a container to receive the incoming files
list.data<-list()

# create a loop to read in your data
for (i in 1:length(list.filenames))
{
  list.data[[i]]<-read.csv(list.filenames[i])
}

# add the names of your data to the list
names(list.data)<-list.filenames

# or this
list.data[1]