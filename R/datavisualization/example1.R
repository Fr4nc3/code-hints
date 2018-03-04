##########################################
# Francia Riesco 
# 01/20/2018
# #1
##########################################
getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') #[1]

# (1) Save the data to excel and read into R for analysis. 
# I implemented the read of the excel file in this way, because it was more easy copy/paste the table in excel  
# and read it from R and load as a single vector
library(xlsx)
data <- read.xlsx("hospital_days.xlsx",1)
hospital.days = c()
for(i in names(data)){ #[2]
  for (v in data[[i]]) # looping the number from each column
    hospital.days <- c(hospital.days, v)  # add all the entries as one big vector #[3]
}

hospital.days # all the entries


# (2) Make a histogram of the duration of days of hospital stays.  Ensure the histogram is labelled appropriately. 
# Use a width of 1 day.  Describe the shape center and spread of the data.  Are there any outliers? 


#hist(~tl,data=ChinookArg,xlab="Total Length (cm)",w=5)
hist(hospital.days, 
     main="duration of days of hospital stays", 
     xlab="Days", 
     border="blue", 
     col="green",
     breaks=seq(0,15) 
)


five.num <- fivenum(hospital.days) #   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
boxplot(hospital.days, horizontal=TRUE, xaxt="n", col="green")
axis(side=1, at=five.num, labels=TRUE)
text(five.num, rep(1.2,5), srt=90, adj=0, labels=c("Min","Lower Hinge","Median","Upper Hinge","Max")) 
outliers.days <- boxplot(hospital.days, plot = FALSE)$out #oly get the outliers
# (3) Find the mean, median, standard deviation, first and third quartiles, minimum and maximum of the durations of hospital stay in the sample. 
# Summarize these values in a table that you create in EXCEL or WORD. In other words, do *not* simply copy and paste R output. 
# Given the shape of the distribution, what is the best single number summary of the center of the distribution?  
# What is the best single number summary of the spread of the distribution? 

fivenum(hospital.days)
mean(hospital.days)
median(hospital.days)
sd(hospital.days)
summary(hospital.days)
min(hospital.days)
max(hospital.days)
sort(outliers.days)

# (4) Assume that the literature on this topic suggests that the distribution of days of hospital stay are normally 
# distributed with a mean of 5 and a standard deviation of 3.  Use R to determine the probabilities below based on the normal distribution:
#   (a) What percentage of patients are in the hospital for less than a week? 
pnorm(7,5,3)
#   (b) Recent publications have indicated that hypervirulent strains of C. Difficile are on the rise.  
# Such strains are associated with poor outcomes, including extended hospital stays.   
# An investigator is interested in showing that the average hospital stay durations have increased versus published literature. 
# He has a sample of 10 patients from his hospital.  If the published data are consistent with the truth, what is the probability that the sample 
# mean in his sample will be greater than 7 days? 
# 
1-pnorm(7,5, 3/sqrt(10))



# REFERENCES
# [1] https://stackoverflow.com/questions/30738974/rjava-load-error-in-rstudio-r-after-upgrading-to-osx-yosemite
# [2] https://stackoverflow.com/questions/18462736/loop-through-columns-and-add-string-lengths-as-new-columns
# [3] https://stackoverflow.com/questions/22235809/append-value-to-empty-vector-in-r
# [4] http://derekogle.com/fishR/2016-03-10-Histograms-with-w
# [5] https://www.r-bloggers.com/histograms-by-just-defining-bin-width/
# [6] https://www.wikihow.com/Calculate-Outliers
# [7] https://stackoverflow.com/questions/44089894/identifying-the-outliers-in-a-data-set-in-r

# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)