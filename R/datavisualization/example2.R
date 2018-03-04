##########################################
# Francia Riesco 
# 01/25/2018
# #2
##########################################
# (1) Summarize the data by whether children participated in the meal preparation or not.
# Use an appropriately labelled table to show the results.  Also include a graphical presentation 
# that shows the distribution of calories for participants vs. non-participants.  
# Describe the shape of each distribution and comment on the similarity (or lack thereof) 
# between the distributions in each population.
getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') # problem with my rJava library in mac
#summary(data$noparticipants)
library(xlsx) # to read the xml 
data <- read.xlsx("calories_intake.xlsx", 1)
noparticipants<- na.omit(data$noparticipants) # remove the NA fields
summary(data$participants)
sd(data$participants)
summary(noparticipants)
sd(noparticipants)
length(data$participants)
length(noparticipants)

#ggplot histogrqam or the participants 
par(mfrow=c(1, 1)) 
library(ggplot2)
library(ggpubr) # to put two histogram together
part.ggplot <-ggplot(data=data, aes(data$participants)) + 
geom_histogram(aes(y =..density..), 
               #breaks=seq(), 
               bins = 8,
               col="red", 
               fill="green", 
               alpha=.2) + 
geom_density(col=2)+
geom_vline(aes(xintercept=mean(data$participants)), color="blue", linetype="dashed", size=0.5) +
labs(title="Participants: calorie intake for that meal", x="calories", y="Counts")
noparts.mean <-mean(noparticipants)
noparts.mean
#histogram for no particupants
nopart.ggplot <- ggplot(data=data, aes(data$noparticipants)) + 
geom_histogram(aes(y =..density..), 
               #breaks=seq(), 
               bins = 10,
               col="red", 
               fill="green", 
               alpha=.2) + 
geom_density(col=2) + 
geom_vline(aes(xintercept=noparts.mean), color="blue", linetype="dashed", size=0.5) +
labs(title="No Participants: calorie intake for that meal", x="calories", y="Counts")

ggarrange(part.ggplot, nopart.ggplot, 
          labels = c("A", "B"),
          ncol = 2, nrow = 1)



par(mfrow=c(1, 2)) # need 1x1layout

hist(data$participants, 
     main="Participants: calorie intake for that meal", 
     xlab="Calories", 
     border="red", 
     col="green"
)

hist(data$noparticipants, 
     main="No Participants: calorie intake for that meal", 
     xlab="Calories", 
     border="red", 
     col="green"
)

boxplot(data$participants, horizontal=TRUE, xaxt="n", col="green", main="Participants")
axis(side=1, at=fivenum(data$participants), labels=TRUE)
text(fivenum(data$participants), rep(1.2,5), srt=90, adj=0, labels=c("Min","Lower Hinge","Median","Upper Hinge","Max")) 
boxplot(noparticipants, horizontal=TRUE, xaxt="n", col="lightblue", main="no participants")
axis(side=1, at=fivenum(noparticipants), labels=TRUE)
text(fivenum(noparticipants), rep(1.2,5), srt=90, adj=0, labels=c("Min","Lower Hinge","Median","Upper Hinge","Max")) 

#boxplot(data$participants~data$noparticipants)


# (2) Does the mean calorie consumption for those who participated in the meal preparation differ from 425?  
# Formally test at the α=0.05 level using the 5 steps outlined in the module.
#


t.test(data$participants, mu=425,  alternative="two.sided", conf.level=0.95)
qt(0.025, df = 24)

t=(431.39-425)/(105.70/sqrt(25))
t



# (3) Calculate a 90% confidence interval for the mean calorie intake for participants in the meal preparation.
# Interpret the confidence interval.
t.test(data$participants, conf.level = 0.9)

 x <- data$participants
 mean.x <- mean(x)
 SE.x   <- sd(x) / sqrt(length(x))
 mean.int.90 <- mean.x + qt( c(0.05, 0.95), length(x) - 1) * SE.x
 mean.int.90
 

# (4) Formally test whether or not participants consumed more calories than non-participants at the α=0.05 level using the 5 steps
# outlined in the module.
 x1<-431.4 
 x2<-346.8
 s1<-105.7
 s2<-99.50
 n1<-25
 n2<-22
 
 t<-(x1-x2)/sqrt((s1^2/n1)+(s2^2/n2))
 t
 t.test(data$participants,data$noparticipants, alternative="greater", conf.level=0.95)

# (5) Are the assumptions of the test used in (4) met?  How do you know?

#anwered in the document. 


# REFERENCES 
# [] https://www.datacamp.com/community/tutorials/make-histogram-ggplot2
# [] http://www.sthda.com/english/articles/24-ggpubr-publication-ready-plots/81-ggplot2-easy-way-to-mix-multiple-graphs-on-the-same-page/
# [] https://mgimond.github.io/Stats-in-R/CI.html

# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)
  