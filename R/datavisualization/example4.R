##########################################
# Francia Riesco 
# 02/12/2018
# #4
##########################################


# The data on the next two pages is from a Canadian 1970 census which collected information about specific occupations.  
# Data collected was used to develop a regression model to predict prestige for all occupations.  Use R to calculate 
# the quantities and generate the visual summaries requested below.  
# (1) Save the data to excel and read into R for analysis.
getwd()
setwd("") # set up my workenviroment

# I had an rJava error from my mac and I fixed adding this line, I was unable to do it in a different way
dyn.load('/Library/Java/JavaVirtualMachines/jdk1.8.0_151.jdk/Contents/Home/jre/lib/server/libjvm.dylib') # problem with my rJava library in mac

library(xlsx) # to read the xls
data <- read.xlsx("hw4.xlsx", 1)
summary(data)
# (2) To get a sense of the data, generate a scatterplot to examine the association between prestige score and years of education.
# Briefly describe the form, direction, and strength of the association between the variables.  Calculate the correlation.  
x<-data$Education.Level#independent variable
y<-data$Prestige.Score        #dependent variable
xlabel <- "Education Level (years)"
ylabel <- "Prestige Score"
par(mfrow=c(1, 1)) # need 1x1layout
library(ggplot2)
ggplot(data, aes(x=x, y=y)) + 
  geom_point()+
  labs(title="Scatterplot of Education Level vs Prestige Score", x=xlabel, y=ylabel )+
  geom_smooth(method=lm, se=TRUE)
cor(y,x)
cor.test(y,x)

# (3) Perform a simple linear regression.  Generate a residual plot.  Assess whether the model assumptions are met.  
# Are there any outliers or influence points?  If so, identify them by ID and comment on the effect of each on the regression.

lm(y~x)
m<-lm(y~x)
summary(m)

#residual plot
plot(x,resid(m), axes=TRUE, frame.plot=TRUE, xlab = xlabel, ylab="residuals") 
abline(h=0)


model = lm(formula = y ~ x)


summary(model)


abline(model, lwd = 2, col = "red")

# Pull out the residual and fitted values from the model so that we can plot them.
resid = resid(model)
fitted = fitted(model)

# Plot the residuals to check the assumptions.
plot(x = x, y = resid, main = "Residuals vs Education Level (Predictor X)")
abline(h = 0)
plot(x = fitted, y = resid, main = "Residuals vs Predicted Score (yhat)")
abline(h = 0)

hist(x = resid, main = "Residuals", breaks = 20)
plot(density(x = resid), main = "Residuals")

df<- data.frame(resid = resid)
ggplot(data=df, aes(df$resid)) + 
  geom_histogram(aes(y =..density..), 
                 #breaks=seq(), 
                 bins = 10,
                 col="red", 
                 fill="green", 
                 alpha=.2) + 
  geom_density(col=2) + 
  labs(title="Residuals Histogram", x="Residuals", y="Counts")

#used the example from 
# https://stats.stackexchange.com/questions/117873/how-to-detect-outliers-from-residual-plot
# I was able to identify 3 point which they are easy to identify in the plot   s
library(car)

(outs <- influencePlot(m))
n <- 2
Cooksdist <- as.numeric(tail(row.names(outs[order(outs$CookD), ]), n))
Lev <- as.numeric(tail(row.names(outs[order(outs$Hat), ]), n))
StdRes <- as.numeric(tail(row.names(outs[order(outs$StudRes), ]), n))

outs
df <- data.frame(x=x, y=y)

plot(df$x, df$y, xlab = xlabel, ylab = ylabel)
abline(m, col = "blue")
points(df$x[Cooksdist], df$y[Cooksdist], col = "red", pch = 0, lwd = 15)
points(df$x[Lev], df$y[Lev], col = "blue", pch = 25, lwd = 8)
points(df$x[StdRes], df$y[StdRes], col = "green", pch = 20, lwd = 5)
text(df$x[as.numeric(row.names(outs))], 
     df$y[as.numeric(row.names(outs))], 
     labels = paste("", sep ="x", ""),
     pos = 1)

# If there were outliers in the plots, we could sort the residuals to find which observations had
#sort(resid)


# (4) Calculate the least squares regression equation that predicts prestige from education, income and percentage of women. 
# Formally test whether the set of these predictors are associated with prestige at the α= 0.05 level. 
panel.cor <- function(x, y, digits=2, prefix="", cex.cor, ...) {
  usr <- par("usr")
  on.exit(par(usr))
  par(usr = c(0, 1, 0, 1))
  r <- abs(cor(x, y, use="complete.obs"))
  txt <- format(c(r, 0.123456789), digits=digits)[1]
  txt <- paste(prefix, txt, sep="")
  if(missing(cex.cor)) cex.cor <- 0.8/strwidth(txt)
  text(0.5, 0.5, txt, cex = cex.cor * (1 + r) / 2)
}
panel.hist <- function(x, ...) {
  usr <- par("usr")
  on.exit(par(usr))
  par(usr = c(usr[1:2], 0, 1.5) )
  h <- hist(x, plot = FALSE)
  breaks <- h$breaks
  nB <- length(breaks)
  y <- h$counts
  y <- y/max(y)
  rect(breaks[-nB], 0, breaks[-1], y, col="white", ...)
}
panel.lm <- function (x, y, col = par("col"), bg = NA, pch = par("pch"),
                      cex = 1, col.smooth = "black", ...) {
  points(x, y, pch = pch, col = col, bg = bg, cex = cex)
  abline(stats::lm(y ~ x), col = col.smooth, ...)
}

m<-lm(data$Prestige.Score~data$Education.Level+data$Income+data$Percent.of.Workforce.that.are.Women)
summary(m)
anova(m)

x<-data$Education.Level#independent variable
y<-data$Prestige.Score          #dependent variable
df <- data.frame(
                 income = data$Income+data, 
                 prestige.score = data$Prestige.Score,
                 education = data$Education.Level+data,
                 women = data$Percent.of.Workforce.that.are.Women
                   )
pairs(data,upper.panel=panel.cor, diag.panel=panel.hist, lower.panel=panel.lm)
pairs(data)
cor(data)


# (5) If the overall model was significant, summarize the information about the contribution of each variable separately at the same 
# significance level as used for the overall model (no need to do a formal 5-step procedure for each one, just comment on the results of the tests). 
# Provide interpretations for any estimates that were significant.   Calculate 95% confidence intervals where appropriate.
summary(lm(data$Prestige.Score~data$Education.Level))
confint(lm(data$Prestige.Score~data$Education.Level), level = 0.95)

summary(lm(data$Prestige.Score~data$Income))
confint(lm(data$Prestige.Score~data$Income), level = 0.95)

summary(lm(data$Prestige.Score~data$Percent.of.Workforce.that.are.Women))
confint(lm(data$Prestige.Score~data$Percent.of.Workforce.that.are.Women), level = 0.95)



# (6) Generate a residual plot showing the fitted values from the regression against the residuals.  Is the fit of the model reasonable?  
# Are there any outliers or influence points?
confint(m, level = 0.95)
par(mfrow=c(1, 1)) # need 1x1layout
plot(fitted(m),resid(m), axes=TRUE, main="Fitted Values vs Residuals", frame.plot=TRUE, xlab = "fitted values", ylab="residuals")
abline(h=0)

#Checking Normality of residuals
hist(resid(m))
plot(m, pch=16, which=1)

df <- data.frame(resid = resid(m))

ggplot(data=df, aes(df$resid))+ 
  geom_histogram(aes(y =..density..), 
                 col="red", 
                 fill="green", 
                 alpha = .2) + 
  geom_density(col=2) + 
  labs(title="Histogram for Residuals Multiple Regression") +
  labs(x="Residuals", y="Count")
#exclude women percentage
# m<-lm(data$Prestige.Score~data$Education.Level+data$Income)
# summary(m)
# anova(m)
# plot(m, pch=16, which=1)

# REFERENCES 
# [] http://www.r-tutor.com/elementary-statistics/simple-linear-regression/residual-plot
# [] https://www.statmethods.net/stats/regression.html 
# [] https://www.statmethods.net/stats/rdiagnostics.html
# [] http://r-statistics.co/Linear-Regression.html
# [] https://rpubs.com/FelipeRego/MultipleLinearRegressionInRFirstSteps

# Version 1.1.383 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko)
# R version 3.4.2 (2017-09-28) -- "Short Summer"
# Copyright (C) 2017 The R Foundation for Statistical Computing
# Platform: x86_64-apple-darwin15.6.0 (64-bit)