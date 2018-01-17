############################
# Francia Riesco 
# December 11, 2017
############################
# Part1) Confidence Intervals 
# Suppose that the Black Friday spending is normally distributed with mean
# $800 and standard deviation $150.

# a) Generate the data for 5000 shoppers. Draw a sample of size 50 from
# this data. Show the 95.44% confidence interval using this sample.


options(digits=4)

set.seed(150)

pop.mean <- 800 # mean $800
pop.sd <- 150 # sd $1500

x <- rnorm(5000, mean = pop.mean, sd = pop.sd)
x <- as.integer(x)

sample.size <- 50 #sample size

sd.sample.means <- pop.sd/sqrt(sample.size)
sd.sample.means

sample.data <- sample(x, size=sample.size)
sample.data

xbar <- mean(sample.data)
xbar

cat("95.44% Conf Interval = ", xbar - 2*sd.sample.means, "-", xbar + 2*sd.sample.means, "\n")

# From the above, we can be 95.44% confident that the mean score of all shoppers lies between $733.7 - $818.5 .

# b) Draw 100 samples from the above data. Plot the confidence intervals for
# these 100 samples. Determine how many samples do not have the
# population mean within their 95.44% confidence intervals?

samples <- 100

xbar2 <- numeric(samples)

for (i in 1: samples) {
  sample.data.1 <- sample(x, size=sample.size)
  xbar2[i] <- mean(sample.data.1)
  str <- sprintf("%2d: xbar = %.2f, CI = %.2f - %.2f",
                 i, xbar2[i], xbar2[i] - 2*sd.sample.means,
                 xbar2[i] + 2*sd.sample.means)
  cat(str,"\n")
}
xbar2
# number outside the range
sum(abs(xbar2-pop.mean) > 2*sd.sample.means)

matplot(rbind(xbar2 - 2*sd.sample.means, xbar2 + 2*sd.sample.means),
        rbind(1:samples, 1:samples), type="l", lty=1)
abline(v = pop.mean)

# c) Using the sample from a), compute the confidence intervals and
# precisions for the confidence levels 75%, 85%, 95%, and 99%,
# respectively.
plot.confidence <- function (conf = 95) { # this methid create the graph for the percentages
  alpha <- 1 - conf/100
  z <- qnorm(1 - alpha/2)
  print(z, digits=4)
  
  f1 <- curve(dnorm(x), from=-3, to=3, 
              xaxt="n", yaxt="n",
              xlab = "z")
  
  title(paste("Confidence =", conf, "%"))
  
  axis(side=1, at=c(-z, 0, z), las=0,
       labels=formatC(c(-z, 0, z), digits=3))
  
  polygon(f1$x, f1$y, col="lightblue")
  
  x.1 <- seq(-3, -z, by = 0.05)
  y.1 <- dnorm(x.1)
  x.1 <- c(x.1, -z, -z)
  y.1 <- c(y.1, dnorm(-z), dnorm(-3))
  
  polygon(x.1, y.1, col="white")
  
  x.2 <- seq(3, z, by = -0.05)
  y.2 <- dnorm(x.2)
  
  x.2 <- c(x.2, z, z)
  y.2 <- c(y.2, dnorm(z), dnorm(3))
  
  polygon(x.2, y.2, col="white")
  
  # lines(c(0,0), c(dnorm(-3), dnorm(0)), lty=2)
  
  text(0, 0.2, 1-alpha)
  text(-2.6, 0.2, alpha/2)
  text(2.6, 0.2, alpha/2)
  
  return (z)
}

conf <- c(75, 85, 95, 99)
conf

alpha <- 1 - conf/100
alpha

qnorm(alpha/2)

qnorm(1 - alpha/2)

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), z: %.2f , %.2f",
                 100*(1-i), i, 
                 qnorm(i/2),
                 qnorm(1-i/2))
  cat(str,"\n")
}


par(mfrow = c(4,1))
for (i in conf) plot.confidence(i)
par(mfrow = c(1,1))

sample.data

sd.sample.means <- pop.sd/sqrt(sample.size)
sd.sample.means

xbar <- mean(sample.data)
xbar

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), CI = %.2f - %.2f",
                 100*(1-i), i, 
                 xbar - qnorm(1-i/2) * sd.sample.means,
                 xbar + qnorm(1-i/2) * sd.sample.means)
  cat(str,"\n")
}

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), Precision = %.2f",
                 100*(1-i), i, 
                 2* qnorm(1-i/2) * sd.sample.means)
  cat(str,"\n")
}



# d) For the 90% confidence level, what is the margin of error with the
# sample used in a). What sample sizes are needed to have the margin of
# error value of 5, 2, and 1, respectively?


conf <- 90 # 90% confidence level 

alpha <- 1 - conf/100
alpha

pop.sd
sample.size

sd.sample.means <- pop.sd/sqrt(sample.size)
sd.sample.means

qnorm(alpha/2)

qnorm(1 - alpha/2)

error <- qnorm(1 - alpha/2) * sd.sample.means
error

for (error in  c(5.0, 2.0, 1.5)) { #5 , 2, 1 margin error
  required.size <- (qnorm(1 - alpha/2) * pop.sd/error)^2
  required.size <- round(required.size)
  str <- sprintf("Error = %.2f, Required sample size = %d", 
                 error, required.size)
  cat(str, "\n")
}



# Part2) Hypothesis Tests
# Use the data from Part1.
# a) For the two-tailed test, what is the null hypothesis and alternative
# hypothesis for the population mean?
#The null hypothesis is H0: u=800. The alternative hypothesis is Ha:μ != 800. The z-test statistic is computed as shown below:
# 

xbar <- mean(sample.data)
xbar # 776.1
mu0 <- pop.mean # 800
sigma <- pop.sd # 150

n <- sample.size # 50

z <- (xbar - mu0) / (sigma / sqrt(n))
z
# > z
# [1] -1.128
alpha <- 0.05
c(qnorm(alpha/2), qnorm(1 - alpha/2))

#Ha:μ !=μ0 , i.e., the population mean is different from the specified value (two-tailed test)
# The test statistic, z,  lies in between the critical values in the above example. Hence the null hypothesis is not rejected for the given significance level.

# b) Using the critical-value approach, and the sample used in Part1a, show
# the results for significance levels 0.1, 0.05, and 0.01 if the null hypothesis
# should be rejected or not.





# differets significal level
alpha <- 0.10
c(qnorm(alpha/2), qnorm(1 - alpha/2))
#[1] -1.645  1.645
alpha <- 0.05
c(qnorm(alpha/2), qnorm(1 - alpha/2))
#[1] -1.96  1.96 
alpha <- 0.01
c(qnorm(alpha/2), qnorm(1 - alpha/2))
#[1] -2.576  2.576

#The test statistic, z,  lies in between the critical values of the significance levels  0.1, 0.05, and 0.01. 
#Hence the null hypothesis is not rejected for the given significance levels.


#REFERENCES 
# Module 6 notes and R samples
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1