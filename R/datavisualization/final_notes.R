#MODULE 1
z = (x-mean)/sd #calculate z 
pop_mean = 67.99 
pop_sd = 1.90

z <- (72 - pop_mean) / pop_sd
p_yellow1 <- pnorm(72, pop_mean, pop_sd)    #using x, mu, and sigma
p_yellow2 <- pnorm(z)    

p_yellow1 # this is the percentage
p_yellow2
p_blue1 <- 1 - p_yellow1 # for the right size of the curve top 10 
# when n >30 sd = pop_sd/n to calculate z

#example 2 10% or similar  find x find z (like p blue)
x = z*sd+mean  
#Assume that the number of days from conception to birth is normally distributed with a mean of 266
# days and a standard deviation of  5 days. What percentage of pregnancies last more than  39
# weeks (273 days)? As a first step, calculate the z-score associated with   39 weeks (273 days).
z = (273-266)/5

#EXAMPLE 3
# Assume that the number of days from conception to birth is normally distributed with a mean of  266
# days and a standard deviation of   5 days. 
# What percentage of pregnancies last more than   39 weeks (273 days)? 
1 - pnorm(273, 266, 5) 

#EXAMPLE 4
# Assume that the number of days from conception to birth is normally distributed with a mean of 266
# days and a standard deviation of   5 days. 
# What is the probability that my pregnancy will be between   261 and 271 days?
pnorm(271, 266, 5) - pnorm(261, 266, 5) 

#EXAMPLE 5
# The heights of women aged  20 to  29
# approximately follow a normal distribution with a mean of  64 inches and a standard deviation of  2
# inches.  What percent of young women are between 60 and 68 inches? 
pnorm(68, 64, 2) - pnorm(60, 64, 2) 

#EXAMPLE 6
#Let s assume that the distribution of gas on a given day in a given town is normally distributed with a mean of $2.30 
#with a standard deviation of $0.20. What proportion of gas stations are charging less than $2.00?
pnorm(2, 2.30, 0.20)


#EXAMPLE 7
#Find the probability that the sample mean is less than 984 
#if a sample of size 100 is taken from a population with a mean of 1000 and a standard deviation of 300
pnorm(984, 1000, 300/sqrt(100)) # sample size MUST be squaredroot

#MODULE 2
#EXAMPLE 1
#What is the critical value from the standard normal distribution associated with a confidence level of 90%?
#this is from the C table

#EXAMPLE 2
# The test statistic from a test of the following hypotheses:
# H0:μ=50
# H1:μ≠50
# was calculated to be z = 1.35.  Calculate the associated p-value
#p = 2*P(z>1.35) # using the table find value of -1.35
2*(1-pnorm(1.35))

#EXAMPLE 3
# The test statistic from a test of the following hypotheses:
# H0:μ=50
# H1:μ>50
# was calculated to be z = 1.35.  Calculate the associated p-value
1-pnorm(1.35)

#EXAMPLE 3
# The test statistic from a test of the following hypotheses:
# H0:μ=50
# H1:μ<50
# was calculated to be z = 1.35.  Calculate the associated p-value
pnorm(1.35)

#EXAMPLE 4 
# It is known that the population standard deviation is 1.5 inches generally for the month of interest.
# 49 instruments that measure rainfall were placed throughout the county randomly. 
# The sample mean from the instruments was 5.2 inches.  
# Calculate a 95% confidence interval for the population mean of rainfall last month in the county. 
a <- 5.2
s <- 1.5
n <- 49
error <- qt(0.975,df=n-1)*s/sqrt(n) #here 0.975 means  the tail 2.5 each side that is why 0.975
left <- a-error
right <- a+error
left
right

#EXAMPLE 5
#The 95% confidence interval for the population mean was calculated based on a random sample of size  
# n=100 as  55 to  65 What was the sample mean? 
# L=mean-z*sd/sqrt(n)
# R=mean+z*sd/sqrt(n)
# R-z*sd/sqrt(n)=mean
# L+z*sd/sqrt(n)=mean
L= 55
R=65
n=100
z=1.960
sd =(sqrt(n)*(R-L))/(2*z)
mean = L+z*sd/sqrt(n)
sd
mean
#Maybe. Approximately  95% of the time, our  95% confidence interval will contain the true value of the parameter.

#EXAMPLE 6
# H0:μ=100 mg (the mean levels are as labelled)
# H1:μ≠100 mg (the mean levels are not as labelled)
# Assume that the population standard deviation of drug levels is 5 mg. 
# For testing, they take a sample of 10 pills randomly from the manufacturing lines and would like to use a significance level of α=0.05.
# They find that the sample mean is 104 mg. Calculate the z statistic.

#z=sample_mean-population_mean/sample_sd/sqrt(n)

z=(104-100)/(5/sqrt(10))
z
# find the p-value 
2*(1-pnorm(z)) # this is the formula of ≠
#Reject the null hypothesis, the mean levels are not as labeled.


#EXAMPLE 7
# The one samplet-statistic for testing
# H0:μ=10
# H1:μ≠10
# From a sample of  n= 20 at the  α= 0.05 level should reject  H0
# if the absolute value of  t is greater than or equal to which of the following values? 
qt(0.975, df = 20-1)  #this is alpha/2 

#EXAMPLE 8
#Use table B to find the critical value associated with a probability of 0.90 to its left and 5 degrees of freedom
qt(0.90, df = 5)  # note in the question it said 0.90 AT ITS LEFT

#EXAMPLE 9
# For a particular value of the degrees of freedom, the probability that
# Tis greater than t is is 18%.What is the probability that
# T is between −t andt t?
(1-0.18)-0.18 # this is one of the trick question

#EXAMPLE 10
# A sample of  16 observations were taken from a population of interest. Conduct a test of the following hypotheses at the  
# α = 0.025 level of significance. The sample mean was calculated to be  83 
# and the sample standard deviation was calculated to be  10.
# H0:μ=90
# H1:μ<90
#this is z
(83-90)/(10/sqrt(16))

#EXAMPLE 11
# Healthy subjects aged 18 to 40 participated in a study of eating habits.  
# Subjects were given bags of potato chips and bottled water and invited to snack freely.  
# Was there a difference between men and women in the number of potato chips consumed?  
# Here are the data on grams of potato chips consumed.
# 
# Group	   n	Mean	Standard Deviation
# Males	   9	  38	 15
# Females	 11	  12	 10
# We are interested in calculating a 90% confidence interval for the difference in mean 
# number of potato chips consumed between men and women.  Without using software, what is the 
# appropriate critical value to use in the calculation of the confidence interval?  Hint:   
# Use the approximation used in the module for determining the approximate degrees of freedom.

#the interval 90% (same as the tabele 1.860)

t = qt(0.95, df = 8) #this is from the table 
t

# (x1-x2)-t*sqrt(((s1*s1)/n1) + ((s2*s2)/n2))
# (x1-x2)+t*sqrt(((s1*s1)/n1) + ((s2*s2)/n2))

#calculate t for explain the hypothesis
s1=15
s2=10
x1=38
x2=12
n1=9
n2=11
t=(x1-x2)/sqrt(((s1*s1)/n1) + (s2*s2)/n2)
t

#MODULE 3
#EXAMPLE 1
# A least-squares simple linear regression model was fit predicting duration (in minutes) 
# of a dive from depth of the dive (in meters) from a sample of 12 penguins diving depths and times.
# Calculate the F-statistic for the regression by filling in the ANOVA table.
TotalSS  =30
n = 12
MSres = 2
k=1
regDF= k
resDF= n-k-1

#TotalSS = regSS+resSS
#MSres=resSS/resDF
#R^2=regSS/TotalSS
resSS=MSres*resDF
regSS= TotalSS-resSS
MSreg= regSS/regDF
f=MSreg/MSres
f

#EXAMPLE 2
#Calculate the R-squared value for the regression by filling in the ANOVA table. #from the example 1
regSS/TotalSS

#EXAMPLE 3 
# The shear strength of the bond between two types of propellant is important in the manufacturing of a rocket motor. 
# An investigator is interested in whether the age of the propellant is related to the shear strength? 
#   Data from 20 paired observations were used to fit a a least-squares simple linear regression model predicting shear strength from propellant age (in weeks). 
# The equation for the regression is given by  
# y=1000−38x
# . Use this equation to predict the shear strength of a propellant that is 20 weeks old.  
# equation y=b0+b1x
b0=1000
b1=-38
x=20
y=b0+b1*x
y

#EXAMPLE 4
#Calculate the correlation coefficient for the following data:
x=c(1,2,2,3,4)
y=c(1,2,3,2,4)
cor(x,y)

#EXAMPLE 5
#t=b1/seb1 when we have the b1 and the standard error we can calculate t


#MODULE 4

#EXAMPLE 1
# The association between resting heart rate (independent variable) and diastolic blood pressure (dependent variable) was investigated. 
# A least-squares regression line was fit which gave the following equation:  
# y= 1.2x−20 . One subject had a resting heart rate of  70 and their diastolic blood pressure was  60 . 
# Calculate the residual associated with this subject.
#y=-20+1.2x
#y=b0+b1*x
#yi−(β0+β1*xi)=yi−yihat
xi=70
yi=60
yhat=-20+1.2*xi
b0=-20
b1=1.2
yi-(b0+b1*xi)

#EXAMPLE 2
#A least-squares multiple linear regression model was fit on  49
#yhat=75+3x1+5x2-3x3


TotalSS  =200
n = 49
k=3
regDF= k
resDF= n-k-1
resSS =180

#MSres = 2
#TotalSS = regSS+resSS
#MSres=resSS/resDF
#R^2=regSS/TotalSS
# resSS=MSres*resDF
# regSS= TotalSS-resSS
# MSreg= regSS/regDF

regSS=TotalSS-resSS
MSreg=regSS/regDF
MSres=resSS/resDF
f=MSreg/MSres
f
#EXAMPLE 3
#Calculate the percent of variance in y explained by  x1,x2,x3

regSS/TotalSS

#MODULE 5 

#EXAMPLE 1
# A random survey of 205 drivers measured each driver’s anger score. 
# Higher scores indicated higher propensities for road rage. 
# The average anger scores were calculated for drivers aged 16-25, 26-35, 36-45, 46-55, and 56–65. 
# A one-way analysis of variance was performed to assess whether or not there were differences 
# between anger scores of drivers in the different age categories. 
# The resulting partial ANOVA table is shown below. Calculate the F-statistic.
#w within b between
# ssb
# ssw
# totalSS = ssb+ssw
# ssbDF = k-1
# sswDF = n-k
# MSb = ssb/ssbDF
# MSw = ssw/sswDF 
# f=MSb/MSw


TotalSS = 5200
MSb = 50
n = 205
k = 5
ssbDF = k-1
sswDF = n-k
ssb= MSb*ssbDF
ssw = TotalSS-ssb
MSw = ssw/sswDF
f=MSb/MSw
f

#EXAMPLE 2
#hat is the appropriate decision rule that we should use for the global F-test 
#if we are interested in maintaining a type I error rate that is less than 0.05?
qf(.95, df1=ssbDF, df2=sswDF) 

#EXAMPLE 3
#If we would reject the global null hypothesis and were interested in all of the possible pairwise comparisons, 
#how many additional tests would we have to perform?
k*(k-1) /2

#EXAMPLE 4
# If we were to create dummy variables for age group, how many dummy variables would be needed?
k-1

#EXAMPLE 5
# If we performed 20 different linear regressions at the 0.10 level, 
# how many of these would we expect to show significance by chance?
20*0.10

#MODULE 6

#EXAMPLE 1
# A study of stroke patient who survived 6 months after the stroke found that 6/45 men and 22/63 women lived in an institution
# (e.g., nursing home or assisted living facility).  Is there evidence of a difference in risk of living in an institution after stroke for men versus women? 
# What is the risk difference (using men as the reference group)?
p2 <- 6/45 #men
p1 <- 22/63 #women


p1-p2  #risk difference using men as reference group p2 is the reference group

#EXAMPLE 2
#What is the odds ratio (using men as the reference group)?
(p1/(1-p1))/(p2/(1-p2))  #odds ratio

#EXAMPLE 3
# What is the risk ratio (using men as the reference group)?
p1/p2

#book notes
#p1=49/61
#p2 = 38/62
# prop.test(c(49,38), c(61,62), alternative = "two.sided", conf.level = 0.95, correct = FALSE)
# 
# prop.test(c(22,6), c(63,45), alternative = "two.sided", conf.level = 0.95, correct = FALSE)
# die 


#EXAMPLE 4 
#What is the z-statistic for testing the null hypothesis of 
#H0:p1=p2?
p=(6+22)/(63+45)
z= (p1-p2)/sqrt(p*(1-p)*((1/63)+(1/45)))
z
#EXAMPLE 5
#What is the 95% confidence interval for the risk difference (with men as the reference group)?
z= 1.960 # 95% confidence z
(p1-p2)-z*sqrt(  ((p1*(1-p1))/63)  + ((p2*(1-p2))/45)  )
(p1-p2)+z*sqrt(  ((p1*(1-p1))/63)  + ((p2*(1-p2))/45 ) )

#EXAMPLE 6
#We have 30-day follow-up data on 350 stroke patients and want to investigate whether the risk of recurrent stroke and/or death depends on the type of stroke 
#(cerebral embolism or not).  The results of the simple logistic regression of the dummy variable for cerebral embolism (1 = yes, 0 = no) are shown below.  
#Use the output to calculate the odds ratio for recurrent stroke and/or death for those who had a cerebral embolism versus those who did not?

# parameter estimate    SE     p-value
# b0		   -2.80       0.51    <0.001
# b1       1.87        0.65     0.0040 
#exp(b1*(xa-xb))

b1=1.87
xa=1 #has embolia 
xb=0 #doesn't have embolia

exp(b1*(xa-xb))

#EXAMPLE 6
# We have 30-day follow-up data on 350 stroke patients and want to investigate whether the risk of recurrent stroke and/or death depends on the type of stroke 
# (cerebral embolism or not) and age.  The results of the multiple logistic regression of the dummy variable for cerebral embolism (1 = yes, 0 = no) and age are shown below.
# What is the risk of recurrent stroke/death for a patient without a cerebral embolism who is 60 years of age?
# parameter estimate  SE      p-value
# b0		     -15.32   9.50    0.1.069
# bcerebral   2.07    0.68    0.0024
# bage        0.18.   0.13    0.1840 
# ex = exp(b0+b1*b1risk2+b2*risk2+…)
# p=ex/(1+ex)
ex = exp(-15.32+2.07*0+0.18*60) #*0 is without previus cerebral embolism
p = ex/(1+ex)
p

#EXAMPLE 7
#Calculate the odds ratio comparing the odds of recurrent stroke/death for a patient who is 65 versus 64.
b1=0.18
xa=65 
xb=64 
exp(b1*(xa-xb))

#EXAMPLE 8
#Calculate the odds ratio comparing the odds of recurrent stroke/death for a patient who is 65 versus 55.
b1=0.18
xa=65 
xb=55
exp(b1*(xa-xb))

#EXAMPLE 9
#Calculate the 95% confidence interval for the odds ratio comparing the odds of recurrent stroke/death for patients with a cerebral embolism versus those without.
#exp((b1+-zalfa/2*SEb1)(xa-xb))
#exp((b1-zalfa2*SEb1)*(xa-xb))
#exp((b1+zalfa2*SEb1)*(xa-xb))
zalfa2=1.96
b1 = 2.07
xa=1
xb=0
SEb1=0.68
exp((b1-zalfa2*SEb1)*(xa-xb))
exp((b1+zalfa2*SEb1)*(xa-xb))

#EXAMPLE 10
# A study was conducted to determine key predictors of chromosomal fetal abnormalities.  
# Using the multiple logistic regression model and a cut off selected by the investigator, 
# 78 fetuses were predicted by the model of having an abnormality.  
# However, only 14 of the 78 that were predicted to have the abnormality actually did.   
# Of the 122 fetuses that the model predicted did not have the abnormality, 6 of them actually did.  
# Construct a 2 by 2 table of these results to help you calculate the sensitivity of the model using this cutoff.

#EXAMPLE 11
#Construct a 2 by 2 table of these results to help you calculate the specificity of the model using this cutoff.

#              postive    negative      total
# positive   14             64             78
# negative    6             116           122
# total       20           180         200
# 
sensitive = 14/20
specificity = 116/180

sensitive 
specificity






z.prop = function(x1,x2,n1,n2){
  numerator = (x1/n1) - (x2/n2)
  p.common = (x1+x2) / (n1+n2)
  denominator = sqrt(p.common * (1-p.common) * (1/n1 + 1/n2))
  z.prop.ris = numerator / denominator
  return(z.prop.ris)
}

z.prop(30, 65, 74, 103)


#size of the sample to have an error m, z is interval z 
#n=(z*sd/m)^2

