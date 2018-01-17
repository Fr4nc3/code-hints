############################
# Francia Riesco 
# December 3, 2017
############################
library(prob)
library(sampling)
options(digits=10) # used to see the decimal values in the queries part2 [4]
# Part1) Central Limit Theorem 
# The input data consists of the sequence from 1 to 20 (1:20). Show the following three
# plots in a single row.
# a) Show the histogram of the densities of this distribution.
par(mfrow=c(1, 3)) # plot the 3 histogram in one row [2]                ### Thank you for using this! You are one of ONLY 2 students who actually use it!!!

seq <- seq(1, 20)
hist(seq, prob=TRUE,  main = "Histogram of 1:20") #[1]

# b) Using all samples of this data of size 2, show the histogram of the densities of the
# sample means.
samples <- urnsamples(seq, 2)
#samples
xbar.size2 <- (samples$X1 + samples$X2)/2
xbar.size2
hist(xbar.size2, prob = TRUE, main = "Histogram of size 2")



# c) Using all samples of this data of size 5, show the histogram of the densities of the
# sample means.

samples <- urnsamples(seq, 2)
#samples
xbar.size5 <- (samples$X1 + samples$X2)/2
xbar.size5
hist(xbar.size5, prob = TRUE, main = "Histogram of size 5")

# d) Compare of means and standard deviations of the above three distributions.
data.info <- data.frame( mean = c(
  mean(seq),
  mean(xbar.size2),
  mean(xbar.size5)
),
sd = c(
  sd(seq),
  sd(xbar.size2),
  sd(xbar.size5)
))
data.info 

#The mean for each of the sample mean distributions remains the same as the mean of the data,
# while the standard deviation decreases as the sample size increases. # Module 5 notes


# Part2) Central Limit Theorem 
# The data in the file queries.csv contains the number of queries Google has had each day for a one
# year period (365 days). The data file is also available at
# http://kalathur.com/cs544/data/queries.csv. Use this link to read the data using read.csv function
# when submitting the homework.
set.seed(101)
data.queries <- read.csv("queries.csv") #[3]
data.queries <- as.numeric(unlist(data.queries))  # convert entries in numeric          ### Also, you could scale down by dividing by million ()
data.queries

# a) Show the histogram of the distribution of the number of queries. Compute the mean and
# standard deviation of the number of queries Google has had per day.

sample.mean <- mean(data.queries)
sample.sd <- sd(data.queries)

par(mfrow=c(1, 1)) # need 1 layout
hist(data.queries, prob=TRUE, main = "Histogram of Google Queries", breaks = 20) # I have to put breaks because I was havin g issues with the ylim

# b) Draw 1000 samples of this data of size 5, show the histogram of the densities of the sample
# means. Compute the mean of the sample means and the standard deviation of the sample means.


samples <- 1000
sample.size <- 5

xbar <- numeric(samples)

for (i in 1:samples) {
  xbar[i] <- mean(sample(data.queries, sample.size)) # what I did here is create a sample size 5 for each element of the 1000 entry []5
}
#xbar
par(mfrow=c(1, 1)) # need 1 layout
hist(xbar, prob = TRUE, main = "Histogram of size 5 Google Queries",  breaks = 100)

sample.mean5<-mean(xbar)
sample.mean5
sample.sd5<-sd(xbar)
sample.sd5

# c) Draw 1000 samples of this data of size 20, show the histogram of the densities of the sample
# means. Compute the mean of the sample means and the standard deviation of the sample means.


sample.size <-20

xbar <- numeric(samples)

for (i in 1:samples) {
  xbar[i] <- mean(sample(data.queries, sample.size)) # what I did here is create a sample siz 20 for each element of the 1000 entry
}
#xbar
par(mfrow=c(1, 1)) # need 1 layout
hist(xbar, prob = TRUE, main = "Histogram of size 20 Google Queries", breaks = 25)

sample.mean20<-mean(xbar)
sample.mean20
sample.sd20<-sd(xbar)
sample.sd20

# d) Compare of means and standard deviations of the above three distributions.
data.info <- data.frame( mean = c(
  sample.mean, 
  sample.mean5,
  sample.mean20
),
sd = c(
  sample.sd,
  sample.sd5,
  sample.sd20
))
data.info 

# Part3) Central Limit Theorem – Negative Binomial distribution (20 points)
# Suppose the input data follows the negative binomial distribution with the
# parameters size = 5 and prob = 0.5.
# a) Generate 1000 random numbers from this distribution. Show the barplot
# with the proportions of the distinct values of this distribution.
size <- 5
prob <- 0.5
randnumber <- 1000

data.negative <- rnbinom(randnumber, size=size, prob=prob) #6
data.proportions <- prop.table(table(data.negative))
barplot(data.proportions, main="Proportions of the distinct values")

# b) With samples sizes of 10, 20, 30, and 40, generate the data for 5000
# samples using the same distribution. Show the histograms of the densities
# of the sample means. Use a 2 x 2 layout.
par(mfrow = c(2, 2)) # layout 2x2

randnumber <- 5000

negative.data1 <- rnbinom(randnumber, size=10, prob=.5)
negative.data2 <- rnbinom(randnumber, size=20, prob=.5)
negative.data3 <- rnbinom(randnumber, size=30, prob=.5)
negative.data4 <- rnbinom(randnumber, size=40, prob=.5)

hist(negative.data1, prob=TRUE)
hist(negative.data2, prob=TRUE)
hist(negative.data3, prob=TRUE)
hist(negative.data4, prob=TRUE)



# c) Compare of means and standard deviations of the data from a) with the
# four sequences generated in b).
data.info <- data.frame( mean = c(
  mean(data.negative),
  mean(negative.data1),
  mean(negative.data2),
  mean(negative.data3),
  mean(negative.data4)

),
sd = c(
  sd(data.negative),
  sd(negative.data1),
  sd(negative.data2),
  sd(negative.data3),
  sd(negative.data4)
))
data.info 



# Part4) Sampling 
# Use the MU284 dataset from the sampling package. Use a sample size of
# 20 for each of the following.
data(MU284)

# a) Show the sample drawn using simple random sampling without
# replacement. Show the frequencies for each region (REG). Show the
# percentages of these with respect to the entire dataset.
set.seed(123)

n <- 20
N <- nrow(MU284)
randset <- srswor(n, N)
dataset <-MU284[randset  != 0,] 
dataset
reg.table <-table(dataset$REG)
reg.proportions <-prop.table(reg.table)            ### What you did here is finding % of the reg.table. 
                                                   ### What you want to find is that % of those with respect to the "entire dataset." 
                                                   ### table(dataset$REG)/table(MU284$REG)    (-6 pts for a,b,c)
reg.proportions


# b) Show the sample drawn using systematic sampling. Show the
# frequencies for each region (REG). Show the percentages of these with
# respect to the entire dataset.

set.seed(113)

k <- ceiling(N / n) # from a)
k

r <- sample(k, 1)
r
# select every kth item

s <- seq(r, by = k, length = n)

sample.3 <- MU284[s,]
reg.table <-table(sample.3$REG)
reg.proportions <-prop.table(reg.table)
reg.proportions


# c) Calculate the inclusion probabilities using the S82 variable. Using these
# values, show the sample drawn using systematic sampling. Show the
# frequencies for each region (REG). Show the percentages of these with
# respect to the entire dataset.
set.seed(133)

pik <- inclusionprobabilities(MU284$S82, n)
length(pik)
sum(pik)

s <- UPsystematic(pik)
sample.4 <-  MU284[s != 0, ]
table(sample.4$REG)

reg.table <-table(sample.4$REG)
reg.proportions <-prop.table(reg.table)
reg.proportions



# d) Order the data using the REG variable. Draw a stratified sample using
# proportional sizes based on the REG variable. Show the frequencies for
# each region (REG). Show the percentages of these with respect to the
# entire dataset.

sorted.mu284 <- MU284[order(MU284$REG),]  
mu284.frequency <- table(sorted.mu284$REG)
st.sizes <- 20 * mu284.frequency / sum(mu284.frequency)
st.sizes

st.sizes <- as.vector(st.sizes)
st.sizes <- st.sizes[st.sizes != 0]
st.sizes

sample.st <- strata(sorted.mu284, stratanames = "REG", size = st.sizes, method = "srswor", description=TRUE)

reg.table <-table(sample.st$REG)
reg.proportions <-prop.table(reg.table)
reg.proportions


# e) Compare the means of RMT85 variable for these four samples with the
# entire data.
MU284$RMT85
rmt85.mean <- mean(MU284$RMT85, na.rm=TRUE) # ignore NA values
dataset.mean <- mean(dataset$RMT85, na.rm=TRUE)
sample.3.mean <- mean(sample.3$RMT85, na.rm=TRUE)
sample.4.mean <- mean(sample.4$RMT85, na.rm=TRUE)

#sample.st.mean <- mean(sample.st$RMT85, na.rm=TRUE)
sample.st # missing the RMT85 Variable
mu.st.id_unit <-MU284[sample.st$ID_unit,] #collected from the main data with the only variably reliable from the existing data ID_UNIT which seams to be  unique
sample.st.mean <- mean(mu.st.id_unit$RMT85, na.rm=TRUE)


data.info <- data.frame( mean = c(
  rmt85.mean,
  dataset.mean,
  sample.3.mean,
  sample.4.mean,
  sample.st.mean
))
data.info 


#REFERENCES 
#[1] http://www.cookbook-r.com/Graphs/Histogram_and_density_plot/ 
#[2] https://www.statmethods.net/advgraphs/layout.html
#[3] https://stackoverflow.com/questions/6299220/access-a-url-and-read-data-with-r
#[4] https://stackoverflow.com/questions/26734913/r-converting-from-string-to-double
#[5] https://www.rdocumentation.org/packages/base/versions/3.4.1/topics/sample
#[6] https://rstudio-pubs-static.s3.amazonaws.com/265031_74567a40d72347478ff3a089cc6d499e.html

# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1