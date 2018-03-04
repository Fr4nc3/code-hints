##########################################
# Francia Riesco 
# 02/26/2018
# #6
##########################################

getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') # problem with my rJava library in mac

library(xlsx) # to read the xls
data <- read.xlsx("body_rate.xlsx", 1)
summary(data)



# (1) We are interested in whether the proportion of men and women with body temperatures greater than or equal to 98.6 degrees Fahrenheit are equal. 
# Therefore, we need to dichotomize the body temperature variable. Create a new variable, called "temp_level" in which temp_level = 1 
# if body temperature >= 98.6 and temp_level=0 if body temperature < 98.6. 

data$temp_level<-ifelse(data$temp >= 98.6, 1, 0)
head(data)
# (2) Summarize the data relating to body temperature level by sex. 
library(plyr)
ddply(data, "sex", summarise,
      N    = length(temp),
      mean = mean(temp),
      sd   = sd(temp) )

# (3) Calculate the risk difference.  Formally test (at the α=.05 level) whether the proportion of people with higher body temperatures 
# (greater than or equal to 98.6) is the same across men and women, based on this effect measure.  
# Do females have higher body temperatures than males? 
women.success <- subset(data, temp_level == 1 & sex==2)
women.failure <- subset(data, temp_level == 0 & sex==2)
nrow(women.success)
nrow(women.failure)
men.success <- subset(data, temp_level == 1 & sex==1)
men.failure <- subset(data, temp_level == 0 & sex==1)
nrow(men.success)
nrow(men.failure)


prop.test(c(nrow(men.success), nrow(women.success)), c(65,65), alternative = "two.sided",
          conf.level = 0.95, correct = FALSE)
p1 <- nrow(men.success)/65
p2 <- nrow(women.success)/65
nrow(data)
p<-(nrow(men.success)+nrow(women.success))/nrow(data)
z<- (p1-p2)/sqrt(p*(1-p)*(1/65+1/65))

z 

p1
p2

p1-p2  #risk difference
p1/p2  #risk ratio
p2/p1
(p1/(1-p1))/(p2/(1-p2))  #odds ratio

data$sex1<-ifelse(data$sex == 1, "M", "F")
#data
# (4) Perform a logistic regression with sex as the only explanatory variable.  Formally test (at the α=.05 level) 
# if the odds of having a temperature greater than or equal to 98.6 is the same between males and females.   
# Include the odds ratio for sex and the associated 95% confidence interval based on the model in your summary and interpret this value.  
# What is the c-statistic for this model? 

#simple logistic regression model 
m<-glm(data$temp_level ~ data$sex1, family = binomial)
summary(m)

exp(cbind(OR = coef(m), confint.default(m)))
fit2 <- glm(data$temp_level ~ data$sex1-1, family="binomial")
exp(cbind(Odds=coef(fit2), confint(fit2)))

exp(m$coefficients[2]*10)
exp((m$coefficients[2]- qnorm(0.975)*summary(m)$coefficients[2,2])*10)
exp((m$coefficients[2]+ qnorm(0.975)*summary(m)$coefficients[2,2])*10)

library(pROC)
predpr <- predict(m, type=c("response"))
g <- roc(data$temp_level ~ predpr)
plot(g) 
plot(1-g$specificities, g$sensitivities, type = "l",
     xlab = "1 - Specificity", ylab = "Sensitivity", main = "ROC Curve")
abline(a=0,b=1)
grid()

auc(g)
# (5) Perform a multiple logistic regression predicting body temperature level from sex and heart rate.  
# Summarize briefly the output from this model.  Give the odds ratio for sex and heart rate (for a 10 beat increase).  
# What is the c-statistic of this model?  

m<-glm(data$temp_level ~ data$sex1+data$heartrate, family = binomial)
summary(m)

exp(cbind(OR = coef(m), confint.default(m)))
library(aod)
wald.test(b = coef(m2), Sigma = vcov(m2), Terms = 2:4)
predpr <- predict(m, type=c("response"))
g <- roc(data$temp_level ~ predpr)
plot(g) 
plot(1-g$specificities, g$sensitivities, type = "l",
     xlab = "1 - Specificity", ylab = "Sensitivity", main = "ROC Curve")
abline(a=0,b=1)
grid()

auc(g)

exp(m$coefficients[1]+m$coefficients[2]+m$coefficients[3]*10)/(1+exp(m$coefficients[1]+m$coefficients[2]*190+m$coefficients[3]*10))

# (6) Which model fit the data better?  Support your response with evidence from your output.  Present the ROC curve for the model you choose. 
# 



# REFERENCES 
#[1] https://stats.stackexchange.com/questions/136193/from-exp-coefficients-to-odds-ratio-and-their-interpretation-in-logistic-regre

# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)