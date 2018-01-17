############################
# Francia Riesco 
# November 12, 2017
############################



library(prob)

# Part 1) Probability -
# a) From the Bayes’ rule example given in Section 3.10, compute the
# probabilities that a randomly selected non-smoker 
bayes <- function (prior, likelihood) {
  numerators <- prior * likelihood
  return (numerators / sum(numerators)) 
}

prior <- c(0.07, 0.93)
like <- c(0.9, 0.25)         ### Your likelihood is not correct, therefore the output is not correct.  (-5 pts)

output <-bayes(prior, like)


PA1=0.07  #event that the person selected has lung disease
PA2=1-PA1 # 0.93 event that the person selected has no lung disease
PB_A1=0.9       ### What are these?
PB_A2=0.25

# i) has lung disease and
#The probability that a randomly selected smoker has lung disease is:
PA1_B=PA1*PB_A1/(PA1*PB_A1+PA2*PB_A2)
PA1_B
# ii) does not have lung disease. Show the calculations without using R.
#The probability that a randomly selected smoker does not have lung disease is:
PA2_B=PA2*PB_A2/(PA1*PB_A1+PA2*PB_A2)
PA2_B
# Then, verify with the bayes function provided in the samples.
all.equal(output[1], PA1_B) #TRUE two number with floating point [1]
all.equal(output[2], PA2_B) #TRUE

# b) Suppose that in a particular state, among the registered voters, 40% are
# democrats, 50 % are republicans, and the rest are independents. Suppose
# that a ballot question is whether to impose sales tax on internet purchases
# or not. Suppose that 70% of democrats, 40% of republicans, and 20% of
# independents favor the sales tax. If a person is chosen at random that
# favors the sales tax, what is the probability that the person is
# first set up the variables
PD=0.4
PR=0.5
PI=0.1
PT_D=0.7
PT_R=0.4
PT_I=0.2

# i) a democrat?
PD_T= (PT_D*PD)/(PT_D*PD+PT_R*PR+PT_I*PI)
PD_T
# ii) a republican
PR_T= (PT_R*PR)/(PT_D*PD+PT_R*PR+PT_I*PI)
PR_T
# iii) an independent. Show the solutions with the
PI_T=(PT_I*PI)/(PT_D*PD+PT_R*PR+PT_I*PI)
PI_T
# calculations without using R. Then, verify with the bayes function provided
# in the samples.
prior <- c(0.4, 0.5,0.1)
like <- c(0.7,0.4, 0.2)

output <-bayes(prior, like)

output
all.equal(output[1], PD_T) #TRUE two number with floating point
all.equal(output[2], PR_T) #TRUE
all.equal(output[3], PI_T) #TRUE

# Part 2) Random Variables - 

    ###-----------------------------------------------------------------
    ### Without Prof.Kalathur's code below, I don't think your code will run.
    ### if (!is.element("prob", installed.packages()[,"Package"]))
    ### install.packages("https://cran.r-project.org/src/contrib/Archive/prob/prob_0.9-2.tar.gz", repos = NULL, type = "both")
    ### if (!is.element("combinat", installed.packages()[,"Package"]))
    ###install.packages("combinat", dep = TRUE)
    ### Load the library every time to run the following samples
    ### library(prob)
    ### Prob <- prob
    ### ------------------------------------------------------------------

# a) Consider the experiment of rolling a pair of dice. Using R, show how
# would you define a random variable for the absolute value of the difference
# of the two rolls, using a user-defined function.               ### Need to write a function in order to answer these (-4 pts)
S <- rolldie(2, makespace = TRUE)
S <- addrv(S, U = abs(X2-X1)) # I used the example from module 2 notes and from sum random variables [2]
# b) Using the above result, what is the probability that the two rolls differ by
# exactly 2? 
Prob(S, U == 2) 
# What is the probability that the two rolls differ by at most 2?
Prob(S, U <= 2) 
# What is the probability that the two rolls differ by at least 3? Use the Prob
# function of R.
Prob(S, U >= 3) 


# c) Show the marginal distribution of the above random variable (using R).
marginal(S, vars = "U")

# d) Using R, add another random variable to the above probability space
# using a user defined function. The random variable is TRUE if the sum of
# the two rolls is even, and FALSE otherwise. What is the probability that the
# sum of the two rolls is even? Show also the marginal distribution for this
# random variable.
#

IsEven <- function(data) {
 if((data[1]+data[2]) %% 2 == 0) {       # if the sum of the two rolls is even from OH02 hints
  return(TRUE)
}
  return(FALSE)
}

S <- addrv(S,FUN=IsEven, name="TR")
Prob(S,TR)
marginal(S, vars = "TR")



# Part3) Functions - 
# Write your own R function, all.primes(n), that returns a vector of all the
# prime numbers up to n (inclusive). Use the following rules in the function:
# i) Initialize the variable, source, to a vector sequence from 2 to n.

# ii) Initialize the variable, result, to the empty vector, or NULL.
# In a loop, do the following as long as the there are numbers remaining in
# the variable, source.

# iii) take the first element of source.

# iv) concatenate this element to result.

# v) Modify source by eliminating all numbers that are multiples of the
# element taken in step iii). This has to be done in a single statement without
# using any loop.
# After the loop terminates, return the result.


all.primes <- function(n){ 
  source <- 2:n #i # first create an empty vector and if the element is prime I add it to the vector [5]
  result  <- c() # ii empty result vector
  first <- source[1] #iii get the first element 
  result <- c(result, first) # iv add the first element to the result (because 2 is prime)
  source <- source[source%%first!=0] # v remove all the numbers multiple of first element (which is 2) so, they are not prime
  for(i in source){
    if(!any(i %% 2:(i-1) == 0)) #[3] is prime example this works because I already remove 2, this is a loop 
    {
      result <- c(result, i) # add number to the vector if it is prime
    }
  }
  return(result) # return the vector
}

all.primes(200)
all.primes(101) # 101 is prime is included
all.primes(100)
all.primes(15)

#####
# for all primes function I had a different way to do it, without the first element removed result, also I tried do do result<-source[isprime(source)] but I followed the step suggested in the part3
# I think in the requirement  it is missing the point where check if the nomber left in the vector are prime when we go in the loop.
# in other words, my all.primes functions is the best approach to return only primes from a vector with the requirement in the part 3.
###

#REFERENCES 
# [1]http://uc-r.github.io/comparing_numeric_values/ compare two number with floating point
# [2]https://www.codeproject.com/Questions/1214708/R-programming-equals-adding-random-variable
# [3]https://www.programiz.com/r-programming/examples/prime-number 
# [4]https://stackoverflow.com/questions/19767408/prime-number-function-in-r
# [5]https://stackoverflow.com/questions/3413879/how-to-create-an-empty-r-vector-to-add-new-items
# [6]https://stackoverflow.com/questions/9665984/how-to-delete-multiple-values-from-a-vector
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1