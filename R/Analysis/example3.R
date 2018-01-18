############################
# Francia Riesco 
# November 19, 2017
############################

# Part 1) 
# Use the primes (UsingR) dataset. Use the diff function to compute the
# differences between successive primes. Show the frequencies of these
# differences. Show the barplot of these differences.
library(UsingR)

diff.primes<-diff(primes)
table(diff.primes)
barplot(table(diff.primes),ylim=c(0, 100),col="green", xlab="Successive primes difference")          ### Very good!

# Part 2) 
# Use the coins (UsingR) dataset. Do not use explicit loops for any
# calculations. Do not hard code the denominations in the solution. The
# solution should work for any denominations.
attach(coins)
coins # check the shape of coins 

# a) How many coins are there of each denomination?
coins.table <- table(year,value)
apply(coins.table, 2 ,sum)


# b) What is the total value of the coins for each denomination?
denomination<-table(value)*as.numeric(colnames(coins.table))
denomination # total value

# c) What is the total value of all the coins?
sum(apply(denomination, 1 ,sum))


# d) Show the barplot for the number of coins by year.
barplot(apply(coins.table,1,sum),ylim=c(0,50), col="blue", xlab="Year", ylab="Number of coins by year")

# Part 3) 
# Use the south (UsingR) dataset.
# a) Show the stem plot of the data. What do you interpret from this plot?

stem(south)


# b) Show the five number summary of the data. Calculate the lower and
# upper ends of the outlier ranges. What are the outliers in the data?

five.num <- fivenum(south)
five.num
outlier.ranges <-c(five.num[2]-1.5*(five.num[4]-five.num[2]),five.num[4]+1.5*(five.num[4]-five.num[2]))
outlier.ranges # print the outlier ranges

south[south < outlier.ranges[1]]
south[south > outlier.ranges[2]]

# c) Show the horizontal boxplot of the data along with the appropriate labels
# on the plot.
# # 

boxplot(south, horizontal=TRUE, xaxt="n", col="blue")
axis(side=1, at=five.num, labels=TRUE)
text(five.num, rep(1.2,5), srt=90, adj=0, labels=c("Min","Lower Hinge","Median","Upper Hinge","Max")) #[1] [2] # from module 3 example
                                                                                                      ### Very nice with labels!! 



# Part 4) 
# Use the pi2000 (UsingR) dataset.
# a) How many times each of the digits 0 to 9 occur in this dataset? 

pi.frequency <-table(pi2000)
pi.frequency

# b) Show the percentages of their frequencies.

pi.freq.perc <- (pi.frequency/length(pi2000))*100
pi.freq.perc


# c) Show the histogram of the data.

hist(pi2000, col="green")

# Part 5) 
# Suppose that a football (NFL), basketball (NBA), and hockey (NHL)
# games are being shown at the same time. Consider the two-way
# summarized data shown below showing the preferences of men and
# women what sport they wish to watch.


# a) Using cbind, create the matrix for the above data.
matrix<-cbind(c(25,20), c(10,40), c(15,30))
matrix

# b) Set the row names for the data.
gender <- c("Men","Women")
sport <- c("NFL","NBA","NHL")

rownames(matrix)<- gender
matrix
# c) Set the column names for the data.
colnames(matrix) <- sport
matrix

# d) Now, add the dimension variables Gender and Sport to the data.

dimnames(matrix) <- list(Gender=gender, Sport=sport)

# e) Show the marginal distributions for the Gender and the Sport.

margin.table(matrix, 1)
margin.table(matrix, 2)

# f) Show the result of adding margins to the data.

addmargins(matrix)

# g) Show the proportional data separately for Gender and Sport. Interpret
# the results.

prop.table(matrix, 1)


# Men 50% want to watch NFL, 20% of men want to watch NBA and 30% of men want to watch NHL
# Women 22% want to watch NFL, 44% of women want to watch  NBA and 33% of women want to watch NHL 

prop.table(matrix, 2)
# Men want to watch 55%  NFL and women want to watch NFL 44%
# Men want to watch 20% NBA and women want to watch NBA 80%
# Men want to watch 33% NHL and women want to watch NHL 66%

# h) Using appropriate colors, show the mosaic plot for the data. Also show
# the barplot for Gender and Sport separately with the bars side by side. Add
# legend to the plots.
matrix

mosaicplot(matrix, main = "Sport vs Gender", color=c("green", "blue", "cyan")) # [3]

barplot(matrix, beside=TRUE, legend.text=TRUE, col=c("blue","pink"), main= "Gender and Sport")


# Part 6) 
# Use the midsize (UsingR) dataset.
midsize


# a) Show the pair wise plots for all the variables.
summary(midsize)
pairs(midsize, main="Midsize Suv", pch=21) # [4]

# b) Provide at least 4 interpretations of the results.


#1. in early years, Taurus was less popular than Camry or Accord
#2. In 2004 Tourus become more popular than camry or Accord
#3. The sales between Camry and Accord grow similarly thru the years. 
#4. From 2003 to 2004 the sales of Tourus almost double 


# Part 7) 
# Use the MLBattend (UsingR) dataset.
attach(MLBattend)

# a) Extract the wins for the teams BAL, BOS, DET, LA, PHI into the
# respective vectors.
bal <-subset(MLBattend, MLBattend$franchise=="BAL", select="wins") #subset the team and then select only wins rows
bos <-subset(MLBattend, MLBattend$franchise=="BOS", select="wins")
det <-subset(MLBattend, MLBattend$franchise=="DET", select="wins")
la  <-subset(MLBattend, MLBattend$franchise=="LA",  select="wins")
phi <-subset(MLBattend, MLBattend$franchise=="PHI", select="wins")



# b) Create a data frame of five columns using these vectors. Use the team
# names for the columns

mbl.win.data <- data.frame(bal, bos, det, la, phi)
colnames(mbl.win.data) <- c("BAL","BOS","DET","LA","PHI")
mbl.win.data
# c) Show the boxplot of the data frame.

boxplot(mbl.win.data,col=rainbow(8), main="MLB Team Wins")
summary(mbl.win.data)

# d) Provide at least 5 interpretations of the results.

#1.BAL has more wins per a season than any other 4 teams
#2. DET has the lowest wins in a season
#3. BAL, BOS, PHI shared the same minimun number of wins 
#4. BAL has better season than any other 4 team
#5. PHI has the lower mean than any other 4 team



# Part 8)
# Initialize the House and Senate data as shown below:
# house <- read.csv('house.csv', stringsAsFactors = FALSE)
# senate <- read.csv('senate.csv', stringsAsFactors = FALSE)

house <- read.csv('house.csv', stringsAsFactors = FALSE)
senate <- read.csv('senate.csv', stringsAsFactors = FALSE)

#house 
#senate



# Provide the simplest R code for the following:
# a) Show how many senators and house members are there by party lines?
house.party <- table(house$Party)
house.party
senate.party <- table(senate$Party)
senate.party


# b) Show the top 10 states in decreasing order by the number of house
# members in that state?

house.state <-table(house$State) #[8]
sort(house.state,decreasing=T)
head(sort(house.state,decreasing=T), n=10) #[9]
senate.state <-table(senate$State) #[8] # seems senate is meaning less because there are 2 senates per state.
#senate.state
head(sort(senate.state,decreasing=T), n=10) #[9]

# c) Use a box plot on the number of house members per state and
# determine which states are outliers?

boxplot(c(house.state), col="blue",  main="House Member per State")

house.vec <-c(house.state)
five.house <- fivenum(house.vec)
five.house
outlier.ranges.house <-c(five.house[2]-1.5*(five.house[4]-five.house[2]),five.house[4]+1.5*(five.house[4]-five.house[2]))
outlier.ranges.house # print the outlier ranges

house.vec[house.vec < outlier.ranges.house[1]]
house.vec[house.vec > outlier.ranges.house[2]]


# d) What is the average number of years served by party line in the house
# and senate?
summary(senate$Years_in_office)             ### This gives only for senate as a whole.  The question is asking for 'by party (democrats/republican) in the house and senate
                                            
# mean is 9.95 almost 10 years


#REFERENCES 
# [1] https://www.programiz.com/r-programming/box-plot 
# [2] http://www.r-tutor.com/elementary-statistics/numerical-measures/box-plot 
# [3] https://www.tutorialgateway.org/mosaic-plot-in-r/
# [4] https://www.rdocumentation.org/packages/psych/versions/1.7.8/topics/pairs.panels
# [5] https://www.statmethods.net/management/subset.html 
# [6] http://stat.ethz.ch/R-manual/R-devel/library/base/html/subset.html
# [7] https://www.r-bloggers.com/taking-a-subset-of-a-data-frame-in-r/
# [8] https://stackoverflow.com/questions/19727029/how-do-i-get-a-list-sorted-by-frequency-in-r
# [9] https://stackoverflow.com/questions/12187891/how-to-get-top-n-companies-from-a-data-frame-in-decreasing-order
# [10] https://www.r-statistics.com/tag/boxplot-outlier/
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1
