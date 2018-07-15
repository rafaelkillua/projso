# Generate boxplot.
# BoxPlot about the extra time needed by the processes.

# library
library(ggplot2)
setwd("~/Documents/workspace/projso/lab_scheduling_policies")

extra_time_plot<- function(extra_time_data) {
  
  g_plot <- ggplot(data = extra_time_data, aes(y = extra_time_data$extra_time, x = extra_time_data$priority, group = extra_time_data$priority)) +
    geom_boxplot() +
    ylim(500, 2000) +
    labs(x = "Priority", y = "Extra Time In System")
  
  return(g_plot)
}

wait_time_plot <- function(extra_time_data) {
  g_plot <- ggplot(data = extra_time_data, aes(y = extra_time_data$wait_time, x = extra_time_data$priority, group = extra_time_data$priority)) +
    geom_boxplot() +
    ylim(500, 2000) +
    labs(x = "Priority", y = "Extra Time In System")
  
  return(g_plot)
}

#Round Robin
rr_data = read.table("output/extra_time20_rr.ffd", header = T)

png(filename = "plots/extra_time20_rr.png", width = 600, height = 600, units = "px",res = 120)
extra_time_plot(rr_data)
dev.off()

png(filename = "plots/wait_time20_rr.png", width = 600, height = 600, units = "px",res = 120)
wait_time_plot(rr_data)
dev.off()

#Priority Random
pr_data = read.table("output/extra_time20_pr.ffd", header = T)

png(filename = "plots/extra_time20_pr.png", width = 600, height = 600, units = "px",res = 120)
extra_time_plot(pr_data)
dev.off()

png(filename = "plots/wait_time20_pr.png", width = 600, height = 600, units = "px",res = 120)
wait_time_plot(pr_data)
dev.off()

#XV6

xv6_data = read.table("output/extra_time20_xv6.ffd", header = T)

png(filename = "plots/extra_time20_xv6.png", width = 600, height = 600, units = "px",res = 120)
extra_time_plot(xv6_data)
dev.off()

png(filename = "plots/wait_time20_xv6.png", width = 600, height = 600, units = "px",res = 120)
wait_time_plot(xv6_data)
dev.off()

#Kernel
kr_data = read.table("output/extra_time20_kr.ffd", header = T)
png(filename = "plots/extra_time20_kr.png", width = 600, height = 600, units = "px",res = 120)
extra_time_plot(kr_data)
dev.off()

png(filename = "plots/wait_time20_kr.png", width = 600, height = 600, units = "px",res = 120)
wait_time_plot()
dev.off()

#Boxplot do tempo de espera da prioridade 0 para todas as políticas
temp <- subset(rr_data, rr_data$priority == 0)
rr <- data.frame(group = "Round Robin", value = temp$wait_time)

temp <- subset(kr_data, kr_data$priority == 0)
pu <- data.frame(group = "Priority Updating", value = temp$wait_time)

temp <- subset(pr_data, pr_data$priority == 0)
pr <- data.frame(group = "Priority Random", value = temp$wait_time)

temp <- subset(xv6_data, xv6_data$priority == 0)
xv6 <- data.frame(group = "Xv6 Priority Random", value = temp$wait_time)


plot.data = rbind(rr, pu, pr, xv6)

png(filename = "plots/wait_time_p0.png", width = 600, height = 600, units = "px",res = 120)
ggplot(plot.data, aes(x=group, y=value, group=group)) + geom_boxplot()
dev.off()