############################
# Francia Riesco 
# November 27, 2017
############################

# Part1) Binomial distribution 
# Suppose a pitcher in Baseball has 50% chance of getting a strike-out when
# throwing to a batter. Using the binomial distribution,

# a) Compute and plot the probability distribution for striking out the next 6
# batters.

prob <- 0:6
distribution<-dbinom(prob, size=6, prob=.5)
distribution

plot(prob, distribution, type="h", main="Probability Distribution Strick Out 50%", xlab="striking out the next  batters", ylab="Probability")
points(prob, distribution, pch=20)

# b) Plot the CDF for the above

prob.cdf<-c(0,cumsum(distribution))
prob.cdf.plot<-stepfun(prob, prob.cdf)
cdf<-plot(prob.cdf.plot,  main="Cumulative Distribution Function 50%", verticals=FALSE, pch=20, xlab="x", ylab="CDF") 

# c) Repeat a) and b) if the pitcher has 70% chance of getting a strike-out.

distribution2<-dbinom(prob, size=6, prob=.7)
distribution2
plot(prob, distribution2, type="h", main="Probability Distribution Strike out 70%", xlab="striking out the next  batters", ylab="Probability")
points(prob, distribution2, pch=20)

prob.cdf2<-c(0,cumsum(distribution2))
prob.cdf.plot2<-stepfun(prob, prob.cdf2)
cdf<-plot(prob.cdf.plot2,  main="Cumulative Distribution Function 70%", verticals=FALSE, pch=20,xlab="x", ylab="CDF") 



# d) Repeat a) and b) if the pitcher has 30% chance of getting a strike-out.

distribution3<-dbinom(prob, size=6, prob=.3)
distribution3
plot(prob, distribution3, type="h", main="Probability Distribution Strike out 30%", xlab="striking out the next  batters", ylab="Probability")
points(prob, distribution3, pch=20)

prob.cdf3<-c(0,cumsum(distribution3))
prob.cdf.plot3<-stepfun(prob, prob.cdf3)
cdf<-plot(prob.cdf.plot3,  main="Cumulative Distribution Function 30%", verticals=FALSE, pch=20,xlab="x", ylab="CDF") 


# e) Infer from the shape of the distributions.

#  the graph move depending the probability in the 0.5 the graph is shaped as bell in the middle
# in the 0.7 the graph is a bell shifted to the righ and the data is distributed to the right
# in the 0.3 the graph is a bell shifted to the left and the data is distributed to the left


# Part2) Binomial distribution 
# Suppose that 80% of the flights arrive on time. Using the binomial
# distribution,

# a) What is the probability that four flights will arrive on time in the next 10
# flights?

probability.flights<-dbinom(4, size=10, prob=0.8)
probability.flights


# b) What is the probability that four or fewer flights will arrive on time in the
# next 10 flights?

fewer.flights<-pbinom(4, size=10, prob=0.8)
fewer.flights


# c) Compute the probability distribution for flight arriving in time for the next
# 10 flights.
v<-0:10
arriving.flights<-dbinom(v, size=10, prob=.8)
arriving.flights


# d) Show the PMF and the CDF for the next 10 flights.

plot(v, arriving.flights, type="h", main="Probability Mass Function 10 filights", xlab="x")
points(v, arriving.flights, pch=20)

arriving.cdf <- c(0,cumsum(arriving.flights))
cdf <- stepfun(v, arriving.cdf)
plot(cdf, verticals=FALSE, pch=20, main="Cumulative Distribution Function 10 filights", xlab="x")


# Part3) Poisson distribution 
# Suppose that on average 10 cars drive up to the teller window at your bank
# between 3 PM and 4 PM and the random variable has a Poisson
# distribution. During this time period,

# a) What is the probability of serving exactly 3 cars?
threecars <- dpois(3, lambda=10)
threecars

# b) What is the probability of serving at least 3 cars?
atleastthreecars <- 1-ppois(3, lambda=10)                   ### 1-ppois(2, lambda=10) because 3 should be included ('at least 3'), or ppois 2 w/ lower.tail = FALSE because you want P[X>x]   (-2 pts)
atleastthreecars                                            

# c) What is the probability of serving between 2 and 5 cars (inclusive)?

between2and5cars <- (ppois(5, lambda=10)-ppois(2, lambda=10))           ### -ppois(1,...) beacuse 2 should be included  (-2 pts) 
between2and5cars


# d) Calculate and plot the PMF for the first 20 cars.
c <-0:20
pmf.first.cars <-dpois(c, lambda = 10)
pmf.first.cars
plot(c, pmf.first.cars,type="h", main="Probability Mass Function Plot first 20 cars")
points(c, pmf.first.cars, pch=20)

# Part4) Uniform distribution
# Suppose that your exams are graded using a uniform distribution between
# 60 and 100 (both inclusive).

# a) What is the probability of scoring 
#i) 60? 
scoring60 <- dunif(60, min=60, max=100)
scoring60

#ii) 80? 
scoring80 <-dunif(80, min=60, max=100)
scoring80
#iii) 100?
scoring100 <-dunif(100, min=60, max=100)
scoring100


# b) What is the mean and standard deviation of this distribution?

dist <- 60:100
mean <- sum(dist*dunif(100, min=60, max=100))         ### Thinking too much?   mu=(a+b)/2   sd=sqrt((b-a)^2/12)   (-3 pts)
mean
standard.deviation <- sum((dist-mean)^2*dunif(100, min=60, max=100))
standard.deviation
sqrt(standard.deviation)

# c) What is the probability of getting a score of at most 70?

morethan70 <-punif(70, min=60, max=100)
morethan70


# d) What is the probability of getting a score greater than 80 (use the lower.tail option)?

morethan80 <- punif(80, min=60, max=100, lower.tail=FALSE)
morethan80

# e) What is the probability of getting a score between 90 and 100 (both inclusive)?

between90and100 <- punif(100, min=60, max=100)-punif(90, min=60, max=100)
between90and100 


# Part5) Normal distribution 
# Suppose that visitors at a theme park spend an average of $100 on
# souvenirs. Assume that the money spent is normally distributed with a
# standard deviation of $10.


# a) Show the PDF plot of this distribution covering the three standard
# deviations on either side of the mean.

dist <- seq(60, 140)
pdf <- dnorm(dist, mean=100, sd=10)
plot(dist, pdf, main="Probability Distribution covering the three standard Deviations", xlab="x",ylab="Probability", type="l", xlim=c(60,140)) #[10][11] type l line the shape


# b) What is the probability that a randomly selected visitor will spend more
# than $120?

randomly.selected <- pnorm(120, mean=100, sd=10, lower.tail=FALSE)
randomly.selected

# c) What is the probability that a randomly selected visitor will spend
# between $80 and $90 (inclusive)?

between80and90 <- pnorm(90, mean=100, sd=10)-pnorm(80, mean=100, sd=10)
between80and90
# d) What are the probabilities of spending within one standard deviation, two
# standard deviations, and three standard deviations, respectively?

mean <- 100 
sd   <- 10 
one.sd <- pnorm(mean+sd, mean=mean, sd=sd)-pnorm(mean-sd, mean=mean, sd=sd)
one.sd 
two.sd <- pnorm(mean+2*sd, mean=mean, sd=sd)-pnorm(mean-2*sd, mean=mean, sd=sd)
two.sd
three.sd <- pnorm(mean+3*sd, mean=mean, sd=sd)-pnorm(mean-3*sd, mean=mean, sd=sd)
three.sd

# e) Between what two values will the middle 90% of the money spent will
# fall?

middle90<-qnorm(.90, mean=mean, sd=sd, lower.tail=TRUE)
middle90


# f) Show a plot for 10,000 visitors using the above distribution.

visitors <- rnorm(10000, mean=100, sd=10)
#visitors 
visitors.round <- round(visitors)
visitors.round.table <- table(visitors.round)
visitors.round.table
plot(visitors.round.table, type="h")


# Part6) Exponential distribution
# Suppose your cell phone provider’s customer support receives calls at the
# rate of 18 per hour.

# a) What is the probability that the next call will arrive within 2 minutes?
rate <- 18
callnext2 <- pexp(2/60, rate=rate)
callnext2

# b) What is the probability that the next call will arrive within 5 minutes?

callnext5 <- pexp(5/60, rate=rate) 
callnext5

# c) What is the probability that the next call will arrive between 2 minutes
# and 5 minutes (both inclusive)?

callbetween2and5 <- pexp(5/60, rate=18)-pexp(2/60, rate=rate)
callbetween2and5

# d) Show the CDF of this distribution.

dist <- seq(0, 1, by=1/60)
cdf  <- pexp(dist, rate=rate)
plot(dist, cdf, type="l", main="Cumulative Distribution Function Calls", xlab="x")


#REFERENCES 
#[1] http://www.r-tutor.com/elementary-statistics/probability-distributions
#[2] http://www.r-tutor.com/elementary-statistics/probability-distributions/binomial-distribution
#[3] http://www.r-tutor.com/elementary-statistics/probability-distributions/poisson-distribution
#[5] http://www.r-tutor.com/elementary-statistics/probability-distributions/continuous-uniform-distribution
#[6] http://www.r-tutor.com/elementary-statistics/probability-distributions/exponential-distribution
#[7] http://www.r-tutor.com/elementary-statistics/probability-distributions/normal-distribution
#[8] http://www.r-tutor.com/elementary-statistics/probability-distributions/chi-squared-distribution
#[9] http://www.cyclismo.org/tutorial/R/probability.html
#[10] https://www.statmethods.net/advgraphs/probability.html
#[11] http://seankross.com/notes/dpqr/
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1