library(ggplot2)

setwd("~/Documents/workspace/projso/lab_scheduling_policies")

select_priority <- function(value){
  priority = ifelse(value <= 5, 0,
                ifelse(value <= 10, 1,
                       ifelse(value <= 15, 2, 3)
                )
  )
  return(priority)
}

plot_workload <- function(raw_data) {
  ggplot(data = workload, aes(y = (raw_data$V4 + raw_data$V1), x = select_priority(raw_data$V3), group = select_priority(raw_data$V3))) +
    geom_boxplot() +
    labs(x = "Priority", y = "Expected Time In System")
}

#40 Processos
workload = read.table("input/workload40.ffd", header = F)

png(filename = "plots/workload40.png", width = 600, height = 600, units = "px",res = 120)
plot_workload(workload)
dev.off()

#400 Processos
workload = read.table("input/workload400.ffd", header = F)

png(filename = "plots/workload400.png", width = 600, height = 600, units = "px",res = 120)
plot_workload(workload)
dev.off()

#4000 Process
workload = read.table("input/workload4000.ffd", header = F)

png(filename = "plots/workload4000.png", width = 600, height = 600, units = "px",res = 120)
plot_workload(workload)
dev.off()