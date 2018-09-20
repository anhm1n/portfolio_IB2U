library(dplyr)
library(ggplot2)
library(tidyr)

swim_groups <- read.csv("swimresults.csv", stringsAsFactors = F)

# Create a table on the conditional that the student passed
swim_pass <- filter(swim_groups, Pass == "Y")

swim_levels <- group_by(swim_groups, Level) %>% 
  summarize(average = mean(Age), count = n())

swim_pass_level_male <- swim_pass %>% 
  filter(Sex == "M") %>% 
  group_by(Level) %>% 
  summarize(count = n())

swim_pass_level_fem <- swim_pass %>% 
  filter(Sex == "F") %>% 
  group_by(Level) %>% 
  summarize(count = n())

swim_pass_array <- as.data.frame(full_join(by = "Level", swim_pass_level_male, swim_pass_level_fem))
swim_pass_array[is.na(swim_pass_array)] <- 0
swim_pass_array <- mutate(swim_pass_array, Percentage_Male = count.x / nrow(swim_pass),
                          Percentage_Fem = count.y / nrow(swim_pass))
colnames(swim_pass_array)[c(2, 3)] <- c("Count_Male", "Count_Fem")

write.csv(swim_pass_array, file = "SwimPassArray.csv")

#create data frames of 3 largest levels
y4 <- filter(swim_groups, Level == "Y4")
y3 <- filter(swim_groups, Level == "Y3")
p1 <- filter(swim_groups, Level == "P1")

# create plots to show distribution based on level and sex
ggplot(data = swim_groups) +
  geom_histogram(mapping = aes(x = Age, fill = Level), binwidth = 1) +
  scale_x_continuous(breaks = 1:16) +
  scale_y_continuous(breaks = seq(0, 18, by=2)) +
  labs(title = "Age Distribution of Students by Level")

ggplot(data = swim_groups) +
  geom_histogram(mapping = aes(x = Age, fill = Sex), binwidth = 1) +
  scale_x_continuous(breaks = 1:16) +
  scale_y_continuous(breaks = seq(0, 18, by=2)) +
  labs(title = "Age Distribution of Students by Sex")

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

# Bootstrap to create a vector of randomly generated population means
bootstrap_age <- function(df, diff_age = F) {
  listMeans <- sample(passOrFail, size = nrow(df), replace = T) 
  simDF <- mutate(df, Pass = listMeans)
  if (diff_age == F) {
    mean(simDF[simDF$Pass == "Y", 'Age'], na.rm = T)  
  } else {
    mean(simDF[simDF$Pass == "Y" & simDF$Sex == "M", "Age"], na.rm = T) - 
      mean(simDF[simDF$Pass == "Y" & simDF$Sex == "F", "Age"], na.rm = T)    
  }
}

# Plot and draw confidence interval lines for bootstrap
mean_age_plot <- function(means, avg, class, diff_age = F) {
  CI_vals <- quantile(means, prob=c(0.025,0.975), na.rm = T)
  if (diff_age == F) {
    hist(means, main = paste("Average Passing Ages", class), xlab = "Age")
    abline(v = c(CI_vals, avg[2, 2]), lwd = 3, col = c("blue", "blue", "red"), lty = c(1, 1, 2))
    legend("topright", legend = c(paste0("CI 95% [", round(CI_vals[1], 3), ", ", round(CI_vals[2], 3), "]"), 
                                  paste("Observed Mean:", round(avg[2, 2], 3))), 
          col = c("blue", "red"), lty = c(1, 2, 2), lwd = 2, cex = 0.7)
  } else {
    hist(means, main = paste("Average Passing Age Differences (M - F)", class), xlab = "Age")
    abline(v = c(CI_vals, avg[2, 2] - avg[1, 2]), lwd = 3, col = c("blue", "blue", "red"), lty = c(1, 1, 2))
    legend("topright", legend = c(paste0("CI 95% [", round(CI_vals[1], 3), ", ", round(CI_vals[2], 3), "]"), 
                                  paste("Observed Mean Difference:", round(avg[2,2] - avg[1, 2], 3))), 
           col = c("blue", "red"), lty = c(1, 2, 2), lwd = 2, cex = 0.7)  
  }
}

mean_age_plot(replicate(n = sims, bootstrap_age(y4)), y4_avg, "Y4")
mean_age_plot(replicate(n = sims, bootstrap_age(y3)), y3_avg, "Y3")
mean_age_plot(replicate(n = sims, bootstrap_age(p1)), p1_avg, "P1")

mean_age_plot(replicate(n = sims, bootstrap_age(y4, diff_age = T)), y4_avg, "Y4", diff_age = T)
# mean_age_plot(replicate(n = sims, bootstrap_age(y3, diff_age = T)), y3_avg, "Y3", diff_age = T)
mean_age_plot(replicate(n = sims, bootstrap_age(p1, diff_age = T)), p1_avg, "P1", diff_age = T)

