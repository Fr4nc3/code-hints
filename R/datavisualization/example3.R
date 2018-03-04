##########################################
# Francia Riesco 
# 02/02/2018
# #3
##########################################


# (1) Save the data to excel and read into R for analysis.
getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') # problem with my rJava library in mac

library(xlsx) # to read the xml 
data <- read.xlsx("meal_fishs.xlsx", 1)
summary(data$meal.with.fish)
summary(data$Total.Mercury)
# (2) To get a sense of the data, generate a scatterplot (using an appropriate window, label the axes, and title the graph).
# Consciously decide which variable should be on the x-axis and which should be on the y-axis.  Using the scatterplot, describe the form, 
# direction, and strength of the association between the variables.


#Scatterplot with labs, and controlling axes
plot(data$meal.with.fish,data$Total.Mercury, 
     main="Scatterplot of Meal with fish vs Total Mercury",
     xlab = "Meals with Fish", ylab="Total Mercury" , cex = .9)

# (3) Calculate the correlation coefficient.  What does the correlation tell us?
#Calculate Sample Correlation
cor(data$meal.with.fish,data$Total.Mercury)
cor.test(data$meal.with.fish,data$Total.Mercury)
lm(data$Total.Mercury~data$meal.with.fish)
m<-lm(data$Total.Mercury~data$meal.with.fish)


plot(data$meal.with.fish,data$Total.Mercury, 
     main="Scatterplot of Meal with fish vs Total Mercury",
     xlab = "Meals with Fish", ylab="Total Mercury (mg/g)" , cex = .9)
abline(lsfit(data$meal.with.fish, data$Total.Mercury)$coefficients,col="red")

#with ggplot scatter plot of the data was easier to read 
library(ggplot2)
ggplot(data, aes(x=data$meal.with.fish, y=data$Total.Mercury)) + 
  geom_point()+
  labs(title="Scatterplot of Meal with fish vs Total Mercury", x="Meals with Fish", y="Total Mercury (mg/g)" )
  



# (4) Find the equation of the least squares regression equation, and write out the equation.  
# Add the regression line to the scatterplot you generated above.
r<-cor(data$Total.Mercury,data$meal.with.fish)
sy<-sd(data$Total.Mercury)
sx<-sd(data$meal.with.fish)
meanx <- mean(data$meal.with.fish)
meany <- mean(data$Total.Mercury)
r
sy
sx
meanx 
meany 


b1hat=r*(sy/sx)
b0hat=meany-(b1hat*meanx)
b1hat
b0hat

lsfit(data$meal.with.fish, data$Total.Mercury)$coefficients

ggplot(data, aes(x=data$meal.with.fish, y=data$Total.Mercury)) + 
geom_point()+
labs(title="Scatterplot of Meal with fish vs Total Mercury", x="Meals with Fish", y="Total Mercury (mg/g)" )+
geom_smooth(method=lm, se=TRUE)

# (5) What is the estimate for β_1?  How can we interpret this value?  What is the estimate for β0?  
# What is the interpretation of this value?
lm(data$Total.Mercury~data$meal.with.fish)

# (6) Calculate the ANOVA table and the table which gives the standard error of β ̂_1. 
# Formally test the hypothesis that β_1= 0 using either the F-test or the t-test at the α= 0.10 level.  
# Either way, present your results using the 5 step procedure as in the course notes.  Within your conclusion, 
# calculate the R-squared value and interpret this.  Also, calculate and interpret the 90% confidence interval for β_1.

#Request important summary information from R about the model

anova(m)
summary(m)

confint(m, level = 0.90)
length(data$meal.with.fish)


# REFERENCES 
# [] http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization
# [] http://www.cyclismo.org/tutorial/R/linearLeastSquares.html
# [] https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/lin_reg/


# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)