##########################################
# Francia Riesco 
# 02/20/2018
# #5
##########################################

getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') # problem with my rJava library in mac

library(xlsx) # to read the xls
data <- read.xlsx("students.xlsx", 1)
summary(data)

# (1)	How many students are in each group?  Summarize the data relating to both test score and age by the student group (separately). 
# Use appropriate numerical and/or graphical summaries. 

library(plyr)
ddply(data, "group", summarise,
      N    = length(iq),
      mean = mean(iq),
      sd   = sd(iq) )
ddply(data, "group", summarise,
      N    = length(age),
      mean = mean(age),
      sd   = sd(age) )

math <- subset(data, group == "Math student")
chem <- subset(data, group == "Chemistry student")
phys <- subset(data, group == "Physics student")
summary(math)
summary(chem)
summary(phys)

library(reshape2)
df.m <- melt(data , id.var = "group")
df.m

library(ggplot2)
ggplot(data = df.m, aes(x=variable, y=value)) + geom_boxplot(aes(fill=group))
is.factor(data$group)

boxplot(iq~group, data = data, main = "Test Score by Subject",
        xlab = "Group",
        ylab = "Test Score iq")


library("ggpubr")
ggline(data, x = "group", y = "iq", 
       add = c("mean_se", "jitter"), 
       ylab = "iq", xlab = "students", main="Iq vs students ")
library(dplyr)
group_by(data, group) %>%
  summarise(
    count = n(),
    mean = mean(iq, na.rm = TRUE),
    sd = sd(iq, na.rm = TRUE)
  )

# (2)	Do the test scores vary by student group?  Perform a one way ANOVA using the aov or Anova function in R to assess.  
# Summarize the results using the 5 step procedure.  If the results of the overall model are significant, perform the appropriate 
# pairwise comparisons using Tukey's procedure to adjust for multiple comparisons and summarize these results.


m<-aov(iq~group, data = data)
summary(m)
summary.lm(m)
pairwise.t.test(data$iq, data$group, p.adj = "bonferroni")
TukeyHSD(m)

# plot(TukeyHSD(m, conf.level = 0.99),las=1, col = "red")
# 
# (3)	Create an appropriate number of dummy variables for student group and re-run the one-way ANOVA using the lm function with the newly created dummy variables.
# Set chemistry students as the reference group.  Confirm if the results are the same.  What is the interpretation of the beta estimates from the regression model? 
# 

data$g0<-ifelse(data$group == "Physics student", 1, 0)
data$g1<-ifelse(data$group == "Math student", 1, 0)
data$g2<-ifelse(data$group == "Chemistry student", 1, 0)

m2<-lm(iq~g0+g1, data = data) #group 3 chemestry as reference
summary(m2)

# (4)	Re-do the one-way ANOVA adjusting for age.   Focus on the output relating to the comparisons of test score by student type.  
# Explain how this analysis differs from the analysis in step 2 above (not the results but how does this analysis differ in terms of 
# the questions it answers as opposed to the one above).  Did you obtain different results?  Summarize briefly (no need to go through the 5 -step procedure here). 
# Present the least square means and interpret these. 
# 

m<-aov(age~group, data = data)
summary(m)
summary.lm(m)
pairwise.t.test(data$age, data$group, p.adj = "bonferroni")
TukeyHSD(m)

boxplot(age~group, data = data, main = "age by Subject",
        xlab = "Group",
        ylab = "age")

ggline(data, x = "group", y = "age", 
       add = c("mean_se", "jitter"), 
       ylab = "age", xlab = "students", main=" age vs students ")

m2<-lm(age~g0+g1, data = data) #group 3 chemestry as reference
summary(m2)
group_by(data, group) %>%
  summarise(
    count = n(),
    mean = mean(age, na.rm = TRUE),
    sd = sd(age, na.rm = TRUE)
  )

library(car)
Anova(lm(iq~group+age, data=data), type=3)

Anova(lm(iq~group, data=data))
summary(aov(iq~group, data = data))

library(lsmeans)
options(contrasts=c("contr.treatment","contr.poly"))
m5 <- lm(iq~group+age, data=data)

# Covariate-adjusted/Least Squares means and comparisons
lsmeans(m5, pairwise ~ group, adjust = "none")
lsmeans(m5, pairwise ~ group, adjust = "tukey")
pairwise.t.test(data$iq, data$group, p.adj = "none")

# REFERENCES 
# [] https://stackoverflow.com/questions/14604439/plot-multiple-boxplot-in-one-graph
# [] http://www.sthda.com/english/wiki/one-way-anova-test-in-r 

# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)