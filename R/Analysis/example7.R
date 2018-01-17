##########################################
# Francia Riesco 
# 12/14/2017
##########################################

# Picking the Data Set
# Look into the following sites as an example and select a data set that interests you.
# 1. http://www.dataminingconsultant.com/resources.htm
# 2. http://www.kdnuggets.com/datasets/index.html
# 3. https://www.kaggle.com/datasets
# 4. Any other source of your choice
# Preparing the data
# https://www.kaggle.com/nasa/kepler-exoplanet-search-results
#getwd()


# • Import the data set into R.
# • Document the steps for the import process and any preprocessing had
# to be done prior to or after the import. Any R code used in the process
# should be included.

getwd()
library(googleVis)
exo.data<- read.csv("kepler-exoplanets.csv") #load the data
#typeof(exo.data)
#summary(exo.data)

#KOI = Kepler object of interes
exo.subset <-subset(exo.data, 
                    select=c(kepler_name,koi_disposition,
                             koi_pdisposition,koi_score,
                             koi_period,koi_duration))
exo.subset$has_score <- !is.na(exo.subset$koi_score) # add new variable true or false if the KOI has score assigned
summary(exo.subset)
exo.table <- gvisTable(head(exo.subset, 30)) #30 as a snapshot of the dataset
plot(exo.table)


# Analyzing the data
# • Do the analysis as in Module3 for at least one categorical variable and at least one
# numerical variable. Show appropriate plots for your data.



exo.categorical.table <-  table(exo.subset$koi_pdisposition)
exo.categorical.table
barplot(exo.categorical.table,  main="Exoplanets", 
        ylab="Counts", xlab="pdisposition", col=c("darkblue","red"))


koi_score.data <- table(exo.subset$has_score)
slice.labels <- names(koi_score.data)
slice.percents <- round(koi_score.data/sum(koi_score.data)*100)
slice.labels <- paste(slice.labels, slice.percents)
slice.labels <- paste(slice.labels, "%", sep="")

pie(koi_score.data, main="% has koi_score", labels = slice.labels, 
    col=c("red","darkblue"))

exo.categorical.table.multi <-  table(exo.subset$has_score,exo.subset$koi_pdisposition)
exo.categorical.table.multi
barplot(exo.categorical.table.multi,  main="Exoplanets with Score", legend.text = TRUE,
        ylab="Counts", xlab="pdisposition", col=c("red","darkblue"))


exo.false.positive <-subset(exo.subset, koi_pdisposition == "FALSE POSITIVE") #subset of the false positive KOI ie. no exoplanets
summary(exo.false.positive)
exo.candidates <-subset(exo.subset, koi_pdisposition == "CANDIDATE") # subset of candidates KOI
summary(exo.candidates)
fivenum(exo.candidates$koi_duration)

library(ggplot2)
ggplot(data=exo.candidates, aes(exo.candidates$koi_duration)) + 
  geom_histogram(aes(y =..density..), 
                 col="red", 
                 fill="lightgreen", 
                 alpha=.2) + 
  geom_density(col=2) + 

  scale_x_continuous(limits = c(0.0, 30)) +
  labs(title="Histogram koi_duration", x="duration in hours", y="Count")


# • Pick one variable with numerical data and examine the distribution of the data.
# • Draw various random samples of the data and show the applicability of the
# Central Limit Theorem for this variable.

par(mfrow = c(2, 2)) # layout 2x2
samples <-1000
sample.size <- 10
xbar <- numeric(samples)
for (i in 1:samples) {
  xbar[i] <- mean(sample(exo.candidates$koi_duration, sample.size)) # what I did here is create a sample size 5 for each element of the 1000 entry []5
}
hist(xbar, prob = TRUE,   border="red", col="lightgreen",  
     main="Histogram of size 10 koi_duration", xlab="duration in hours")
lines(density(xbar), col="red", lwd=2) # add a density estimate with defaults
lines(density(xbar, adjust=2), lty="dotted", col="darkgreen", lwd=2) 


sample.mean10<-mean(xbar)
sample.mean10
sample.sd10<-sd(xbar)
sample.sd10

sample.size <- 20
xbar <- numeric(samples)

for (i in 1:samples) {
  xbar[i] <- mean(sample(exo.candidates$koi_duration, sample.size)) # what I did here is create a sample size 5 for each element of the 1000 entry []5
}
#xbar

hist(xbar, prob = TRUE,   border="red", col="lightgreen",  
     main="Histogram of size 20 koi_duration", xlab="duration in hours")

lines(density(xbar), col="red", lwd=2) # add a density estimate with defaults
lines(density(xbar, adjust=2), lty="dotted", col="darkgreen", lwd=2) 

sample.mean20<-mean(xbar)
sample.mean20
sample.sd20<-sd(xbar)
sample.sd20



sample.size <- 30

xbar <- numeric(samples)

for (i in 1:samples) {
  xbar[i] <- mean(sample(exo.candidates$koi_duration, sample.size)) # what I did here is create a sample size 5 for each element of the 1000 entry []5
}
#xbar


hist(xbar, prob = TRUE,   border="red", col="lightgreen",  
     main="Histogram of size 30 koi_duration", xlab="duration in hours")

lines(density(xbar), col="red", lwd=2) # add a density estimate with defaults
lines(density(xbar, adjust=2), lty="dotted", col="darkgreen", lwd=2) 


sample.mean30<-mean(xbar)
sample.mean30
sample.sd30<-sd(xbar)
sample.sd30

sample.size <- 40

xbar <- numeric(samples)

for (i in 1:samples) {
  xbar[i] <- mean(sample(exo.candidates$koi_duration, sample.size)) # what I did here is create a sample size 5 for each element of the 1000 entry []5
}
#xbar
hist(xbar, prob = TRUE,   border="red", col="lightgreen",  #xlim=c(1,6),
     main="Histogram of size 40 koi_duration", xlab="duration in hours")

lines(density(xbar), col="red", lwd=2) # add a density estimate with defaults
lines(density(xbar, adjust=2), lty="dotted", col="darkgreen", lwd=2) 

sample.mean40<-mean(xbar)
sample.mean40
sample.sd40<-sd(xbar)
sample.sd40

data.sampling <- data.frame( 
info = c("Sample size 10", "Sample size 20", 
          "Sample size 30", "Sample size 40"),
mean = c(sample.mean10, sample.mean20, 
         sample.mean30, sample.mean40),
sd   = c(sample.sd10, sample.sd20,
         sample.sd30,sample.sd40))
data.sampling


# • Show how various sampling methods can be used on your data.
par(mfrow = c(1, 1)) # layout 1x1
library(prob)
library(sampling)
#random sampling
set.seed(123)
n <- 20
N <- nrow(exo.candidates)
randset <- srswor(n, N)
dataset <-exo.candidates[randset  != 0,] 
#dataset
reg.table <-table(exo.candidates$koi_duration)
reg.proportions <-prop.table(reg.table)   
# reg.table
# reg.proportions
summary(dataset$koi_duration)
hist(dataset$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Random sampling koi_duration", xlab="duration in hours")
lines(density(dataset$koi_duration), col="red", lwd=2) 


#systematic sampling

set.seed(113)
k <- ceiling(N / n) # from a)
k
r <- sample(k, 1)
r
# select every kth item
s <- seq(r, by = k, length = n)

sample.3 <- exo.candidates[s,]
reg.table <-table(sample.3$koi_period)
reg.proportions <-prop.table(reg.table)

summary(sample.3$koi_duration)
hist(sample.3$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Systematic sampling koi_duration", xlab="duration in hours")
lines(density(sample.3$koi_duration), col="red", lwd=2) 


#inclusion probability 
set.seed(133)
pik <- inclusionprobabilities(exo.candidates$koi_duration, n)
length(pik)
sum(pik)

s <- UPsystematic(pik)
sample.4 <-  exo.candidates[s != 0, ]
table(sample.4$koi_period)
reg.table <-table(sample.4$koi_duration)
reg.proportions <-prop.table(reg.table)
reg.proportions
summary(sample.4$koi_duration)
hist(sample.4$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Inclusion Probability sampling koi_duration", xlab="duration in hours")
lines(density(sample.4$koi_duration), col="red", lwd=2) 




#stratified sample 

sorted.exo <- exo.candidates[order(exo.candidates$koi_pdisposition),]
exo.frequency <- table(sorted.exo$koi_pdisposition)
exo.frequency

st.sizes <- 20 * exo.frequency / sum(exo.frequency)
st.sizes

st.sizes <- as.vector(st.sizes)
st.sizes <- st.sizes[st.sizes != 0]
st.sizes
sample.st <- strata(sorted.exo,  stratanames = c("koi_pdisposition"),
                    size = st.sizes, method = "srswor", description=TRUE)

mu.st.id_unit <-exo.candidates[sample.st$ID_unit,]

summary(mu.st.id_unit$koi_duration)
hist(mu.st.id_unit$koi_duration, prob = TRUE,   border="red", col="lightgreen",
     main="Stratified sampling koi_duration", xlab="duration in hours")
lines(density(mu.st.id_unit$koi_duration), col="red", lwd=2)



#compare sampling

exo.candidates.mean <- mean(exo.candidates$koi_duration, na.rm=TRUE) # ignore NA values
random.sampling.mean <- mean(dataset$koi_duration, na.rm=TRUE)
systematic.sampling.mean <- mean(sample.3$koi_duration, na.rm=TRUE)
inclusion.sampling.mean <- mean(sample.4$koi_duration, na.rm=TRUE)

strata.sampling.mean <- mean(mu.st.id_unit$koi_duration, na.rm=TRUE)
exo.candidates.sd <- sd(exo.candidates$koi_duration, na.rm=TRUE) # ignore NA values

random.sampling.sd <- sd(dataset$koi_duration, na.rm=TRUE)
systematic.sampling.sd <- sd(sample.3$koi_duration, na.rm=TRUE)
inclusion.sampling.sd <- sd(sample.4$koi_duration, na.rm=TRUE)
strata.sampling.sd <- sd(mu.st.id_unit$koi_duration, na.rm=TRUE)

par(mfrow = c(2, 2)) # layout 
hist(dataset$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Random sampling koi_duration", xlab="duration in hours")
lines(density(dataset$koi_duration), col="red", lwd=2) 
hist(sample.3$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Systematic sampling koi_duration", xlab="duration in hours")
lines(density(sample.3$koi_duration), col="red", lwd=2) 
hist(sample.4$koi_duration, prob = TRUE,   border="red", col="lightgreen",  
     main="Inclusion Probability sampling koi_duration", xlab="duration in hours")
lines(density(sample.4$koi_duration), col="red", lwd=2) 
hist(mu.st.id_unit$koi_duration, prob = TRUE,   border="red", col="lightgreen",
     main="Stratified sampling koi_duration", xlab="duration in hours")
lines(density(mu.st.id_unit$koi_duration), col="red", lwd=2)


data.compare.sampling <- data.frame( 
  sample.name = c("exo planets dataset", "random sampling",  "systematic sampling", 
                  "inclusion probability sampling", "stratified sampling"),
  mean = c(exo.candidates.mean,random.sampling.mean, systematic.sampling.mean,
           inclusion.sampling.mean,strata.sampling.mean),
  sd = c(exo.candidates.sd,random.sampling.sd, systematic.sampling.sd, 
         inclusion.sampling.sd,strata.sampling.sd))

data.compare.sampling 


# • For confidence levels of 80 and 90, show the confidence intervals of the mean of
# the numeric variable for various samples and compare against the population
# mean.
plot.confidence <- function (conf = 95) {
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
par(mfrow = c(1, 1))
sample.data <- exo.candidates$koi_duration
n <- length(sample.data)

sd.sample.means <- sd(sample.data)/sqrt(n)
sd.sample.means

xbar <- mean(sample.data)
xbar
conf <- c(80, 90) #80% and 90% levels
conf

alpha <- 1 - conf/100
alpha

qt(alpha/2, df = n-1)

qt(1 - alpha/2, df = n-1)

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), t: %.2f , %.2f",
                 100*(1-i), i, 
                 qt(i/2, df = n-1),
                 qt(1 - i/2, df = n-1))
  cat(str,"\n")
}

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), CI = %.2f - %.2f",
                 100*(1-i), i, 
                 xbar - qt(1 - i/2, df = n-1) * sd.sample.means,
                 xbar + qt(1 - i/2, df = n-1) * sd.sample.means)
  cat(str,"\n")
}

for (i in alpha) {
  str <- sprintf("%2d%% Conf Level (alpha = %.2f), Precision = %.2f",
                 100*(1-i), i, 
                 2* qt(1-i/2, df = n-1) * sd.sample.means)
  cat(str,"\n")
}
for (i in conf) plot.confidence(i)

options(digits=4)

set.seed(150)

pop.mean <- mean(exo.candidates$koi_duration)
pop.sd <- sd(exo.candidates$koi_duration)

x <- exo.candidates$koi_duration
sample.size <- 30

sd.sample.means <- pop.sd/sqrt(sample.size)
sd.sample.means

sample.data <- sample(x, size=sample.size)
sample.data

xbar <- mean(sample.data)
xbar

cat("95.44% Conf Interval = ",
    xbar - 2*sd.sample.means, "-", 
    xbar + 2*sd.sample.means, "\n")

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

#compare koi_duration from exoplanets and false positives objects
summary(exo.candidates$koi_duration)
summary(exo.false.positive$koi_duration)

exo <- data.frame(duration = exo.candidates$koi_duration) #create dataframe
false <- data.frame(duration = exo.false.positive$koi_duration)

exo$variable <- 'candidate' # variable name
false$variable <- 'falsepositive'
exo.false.info <- rbind(exo, false)

#print the plot
ggplot(exo.false.info, aes(duration, fill = variable)) +
scale_x_continuous(limits = c(0.0, 30)) +
geom_density(alpha = 0.2)

ggplot(data = exo.false.info, aes(x=variable, y=duration))  #boxplot
+ geom_boxplot(aes(fill=variable))


# histogram and density
ggplot(exo.false.info, aes(duration, fill = variable)) +
  scale_x_continuous(limits = c(0.0, 30)) +
  geom_density(alpha = 0.2) +
  geom_histogram(alpha = 0.5, aes(y = ..density..), position = 'identity')




#REFERENCES 
# [1] https://www.r-bloggers.com/how-to-make-a-histogram-with-ggplot2/
# [2] https://cran.r-project.org/web/packages/googleVis/vignettes/googleVis_examples.html
# [3] http://www.sthda.com/english/wiki/ggplot2-histogram-plot-quick-start-guide-r-software-and-data-visualization
# [4] https://www.r-bloggers.com/overlapping-histogram-in-r/
# [5] https://stackoverflow.com/questions/1245273/histogram-with-logarithmic-scale-and-custom-breaks
# [6] https://blogs.sas.com/content/graphicallyspeaking/2014/08/18/histograms-on-log-axis/
# [7] https://www.datacamp.com/community/tutorials/make-histogram-ggplot2
# [8] https://plot.ly/ggplot2/geom_density/
# [9] https://www.statmethods.net/graphs/density.html
# [10] http://kanglinxm.blogspot.com/2014/08/plot-two-histograms-together-in-r.html
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1