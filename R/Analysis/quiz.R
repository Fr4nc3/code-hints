#q1
#1 mode 
q <-c(400, 300, 150, 300, 550, 290, 150, 300, 500, 550)
names(sort(-table(q)))[1]

#2 
a <-c(400, 300, 200, 150, 150, 324, 550, 645, 290, 500)
sort(a)
IQR(a)
d <- c(60, 60, 60, 60 ,90 ,90, 100, 100, 100, 100)
mean(d)
sd(d)

#3
median(c(400, 300, 200, 150, 150, 324, 550, 645, 290, 500))
#4
sd(c(8, 9, 9, 11, 13))

#5
70+75+ 85+ 90-80*5

#6
sd(c(1, 2, 3, 4, 5))^2

#7
mean(c(25, 20, 35, 30, 45))
mean(c(10, 40, 30, 20, 50))

median(c(25, 20, 35, 30, 45))
median(c(10, 40, 30, 20, 50))

#8 
sort(c(400, 300, 200, 150, 150, 324, 550, 645, 290, 500))
max(c(400, 300, 200, 150, 150, 324, 550, 645, 290, 500)) - min(c(400, 300, 200, 150, 150, 324, 550, 645, 290, 500))

#9
mean(seq(from = 10, to = 40, by = 10))
median(seq(from = 10, to = 40, by = 10))

mean(seq(from = 10, to = 800, by = 10))
median(seq(from = 10, to = 800, by = 10))

#10
mean(c(400, 300, 200, 150, 150, 325, 550, 645, 290, 500))
library(MASS) #FOR FRACTIONS

#q2
#1
#A basket has a yellow ball, an orange ball, a red ball, a green ball, and a blue ball. In how many
#ways can two unordered balls be selected at random with replacement?
#5,2
#uorder
nsamp(n = 5, k = 2, replace = TRUE, ordered = FALSE)

#2
# A basket has a yellow ball, an orange ball, a red ball, a green ball, and a blue ball. If two balls are
# selected at random without replacement, what is the probability that one of selected balls is red?

b1<-urnsamples(c("y","o","r","g", "b"), size = 2, replace = FALSE, ordered = TRUE)
nrow(b1)
subset(b1, X1 == "r" | X2 =="r")
fractions(nrow(subset(b1, X1 == "r" | X2 =="r"))/nrow(b1))

#3
#From a standard deck of 52 cards, what is the probability of drawing a Spade?
S <- cards(makespace = TRUE)
fractions(nrow(subset(S, suit == "Spade"))/nrow(S))

#4
#When two six-faced dice are rolled, what is the probability that the sum of the rolls is 7?
S <- rolldie(2, makespace = TRUE)
fractions(nrow(subset(S, X1 +X2 == 7))/nrow(S)) #1/6



#5
# A basket has 5 red balls, 3 white balls and 2 blue balls. If a ball is drawn at random, what is the
# probability of getting a white ball or a blue ball?

L <- rep(c("red", "white", "blue"), times = c(5, 3, 2))
L


M <- urnsamples(L, size = 1, ordered = TRUE)
M


S <- probspace(M)
S


fractions(Prob(S, out == "white"| out=="blue"))

#6
#coin is tossed twice. What is the probability of getting at least one head?
S <- tosscoin(2, makespace = TRUE)
S


fractions(Prob(S, isin(S, c('H'))))

#7
# A basket has 2 red balls and 2 blue balls. If two balls are drawn successively at random, what is the
# probability of getting a red ball followed by a blue ball?


L <- rep(c("red",  "blue"), times = c(2,2))
L


M <- urnsamples(L, size = 2, ordered = TRUE)
M


S <- probspace(M)
S

fractions(Prob(S, X1 == "red" & X2=="blue"))

#8
#From a standard deck of 52 cards, what is the probability of drawing a Queen?
S <- cards(makespace = TRUE)
fractions(Prob(S, rank == "Q"))
fractions(nrow(subset(S, rank =="Q"))/nrow(S))


#9
#A basket has 5 red balls, 3 white balls and 2 blue balls. If a ball is drawn at random, what is the
#probability of getting a blue ball?
L <- rep(c("red", "white", "blue"), times = c(5, 3, 2))
L

M <- urnsamples(L, size = 1, ordered = TRUE)
M

S <- probspace(M)
S

fractions(Prob(S,  out=="blue"))

#10
# Suppose a card is drawn from a standard deck of 52 cards. Let A be the event that a king selected,
# and B be the event that a heart is selected. What is the conditional probability P(B|A)?
S <- cards(makespace = TRUE)
A <- subset(S, rank =="K")
A
Prob(A)


B <- subset(S, suit == "Heart")
B
Prob(B)


fractions(Prob(A, given = B)) #P(A|B)
fractions(Prob(B, given = A))#P(B|A) this was the question

#q3 no questions

#Q4
#1 Suppose a discrete random variable has a uniform distribution from 1 to 10. The probability that the random variable is at
#least 5 is
m <- 10
pdf<-dunif(1:m, max=m)
sum(pdf[5:m])

#2 
# Suppose there is a 50% chance that a working person will retire at the age of 65 years. Suppose three working people
# are selected at random. What is the probability that exactly two will be working beyond the age of 65 years?

p <-0.5
fractions(dbinom(2, size = 3, prob = p))

#3
# Suppose that a drug is effective 90% of the time in curing a particular disease. Suppose 4 patients with that disease are
# given that drug. If the success scenario is the cure, what is the probability that exactly one will be cured?

n <- 4
p <- 0.9
fractions(dbinom(1, size = n, prob = p))

#4
# A bank system requires its customers to create a 4 digit pin to access their money through an ATM. Thus for each
# individual there are 10,000 (10^4) possible pin numbers. The bank security personnel want to determine on average,
# how many times a thief would have to guess a customer's pin number before getting it correct. To model this, they use
# the geometric distribution (modeling the number of failures until there is a a success). Using the geometric distribution,
# on average, how many times would a thief have to guess a customer's pin number before getting it correct?

# average = (1-p)/p
p <- 1/10000
(1-p)/p

#8 
# A tech support company monitors finds that on average, 10 computers will malfunction per day. Using the poisson distribution,
# what is the probability that no more than 15 computers will malfunction in any given day?

ppois(15, lambda=10)

#9
# The airport Transportation Security Administration (TSA) has been in the news for long wait times in the airport. To
# determine the average wait time in the airport, TSA wants to model their wait times (in minutes) using a continuous
# uniform distribution with a minimum wait time of 15 minutes and a maximum wait time of 180 minutes. If the TSA wait
# time follows a uniform ~(15, 180) distribution, what is the average wait time?
(180+15)/2
 

































