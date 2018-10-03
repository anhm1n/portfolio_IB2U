library(dplyr)
library(ggplot2)
library(tidyr)

swim_groups <- read.csv("swimresults.csv", stringsAsFactors = F)

# Create data frames of 3 largest levels
y4 <- filter(swim_groups, Level == "Y4")
y3 <- filter(swim_groups, Level == "Y3")
p1 <- filter(swim_groups, Level == "P1")

swim_main <- filter(swim_groups, Level == "Y4" | Level == "Y3" | Level == "P1")

# create plots to show distribution based on level and sex
ggplot(data = swim_groups) +
  geom_histogram(mapping = aes(x = Age, fill = Level), binwidth = 1) +
  scale_x_continuous(breaks = 1:16) +
  scale_y_continuous(breaks = seq(0, 18, by=2)) +
  labs(title = "Students' Ages by Level", x = "Age (1-Year Range)")

ggplot(data = swim_main) +
  geom_boxplot(mapping = aes(x = Level, y = Age, fill = Pass)) +
  coord_flip() +
  labs(title = "Age Distribution by Passing of Main Levels")

# create tibbles to have main levels averages
y4_avg <- group_by(y4, Pass) %>% 
  summarize(average = mean(Age), maximum = max(Age), minimum = min(Age), st_dev = sd(Age))
y3_avg <- group_by(y3, Pass) %>% 
  summarize(average = mean(Age), maximum = max(Age), minimum = min(Age), st_dev = sd(Age))
p1_avg <- group_by(p1, Pass) %>% 
  summarize(average = mean(Age), maximum = max(Age), minimum = min(Age), st_dev = sd(Age))

# Bootstrap, keep students age and Sex, randomize pass fail
passOrFail <- c("Y", "N")
sims <- 10000

# Select the true pass and fails for permutations
y4_passes <- y4[, "Pass"]
y3_passes <- y3[, "Pass"]
p1_passes <- p1[, "Pass"]

# Bootstrap to return randomly generated passing student age
bootstrap_age <- function(df) {
  passing <- sample(passOrFail, size = nrow(df), replace = T) 
  simDF <- mutate(df, Pass = passing)
  mean(simDF[simDF$Pass == "Y", 'Age'], na.rm = T)  
}

# Permute to return randomly generated passing student age
permute_age <- function(df, list_pass) {
  passing <- sample(list_pass, size = nrow(df), replace = F) 
  simDF <- mutate(df, Pass = passing)
  mean(simDF[simDF$Pass == "Y", "Age"], na.rm = T)
}

# Plot and draw confidence interval lines for bootstrap/permutation
mean_age_plot <- function(means, avg, class) {
  CI_vals <- quantile(means, prob=c(0.025,0.975), na.rm = T)
  hist(means, main = paste("Average Passing Ages", class), xlab = "Age")
  abline(v = c(CI_vals, avg[2, 2]), lwd = 3, col = c("blue", "blue", "red"), lty = c(1, 1, 2))
  legend("topright", legend = c(paste0("CI 95% [", round(CI_vals[1], 3), ", ", round(CI_vals[2], 3), "]"), 
                                paste("Observed Mean:", round(avg[2, 2], 3))), 
        col = c("blue", "red"), lty = c(1, 2, 2), lwd = 2, cex = 0.7)
}

# Bootstrap and plot 'sims' times
mean_age_plot(replicate(n = sims, bootstrap_age(y4)), y4_avg, "Y4")
mean_age_plot(replicate(n = sims, bootstrap_age(y3)), y3_avg, "Y3")
mean_age_plot(replicate(n = sims, bootstrap_age(p1)), p1_avg, "P1")

# Permute and plot 'sims' times
mean_age_plot(replicate(n = sims, permute_age(y4, y4_passes)), y4_avg, "Y4")
mean_age_plot(replicate(n = sims, permute_age(y3, y3_passes)), y3_avg, "Y3")
mean_age_plot(replicate(n = sims, permute_age(p1, p1_passes)), p1_avg, "P1")

