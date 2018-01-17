############################
# Francia F. Riesco
# November 5 2017
###########################
# Part1) 
# The following sample data shows the scores of 10 students in an exam:
#   45, 80, 83, 78, 75, 77, 79, 83, 83, 100
scores<-c(45, 80, 83, 78, 75, 77, 79, 83, 83, 100)
scores.length <- length(scores) #  we use the length of the score in several places
# a) Using indexing, show the expression for accessing the first and last items. The code should
# not hardcode the value 10 for the number of items.
scores[c(1, scores.length)]

# b) Using comparison operators, write the expression for scores less than the mean, computed
# as mean(scores).
mean <-mean(scores) # mean value stored in a variable
mean
scores < mean
# c) Using logical indexing and the expression from b), return all the scores that are less than the
# mean.
scores[scores < mean]
# d) Using rep function, create a sequence, as the same length as scores, of alternating TRUE,
# FALSE values. Using this sequence, return every other element from the scores. The code
# should not hardcode the value 10 for the number of scores. You can assume that there are
# even number of values in scores.
scores[rep(c(TRUE,FALSE), times=scores.length/2)] #asume scores.length as even number

# e) Using the paste function with LETTERS, show the code for the following output.
# The code should not hardcode the value 10 for the number of scores.
paste(LETTERS[1:scores.length], scores, sep="=") 

# f) Create a matrix of size 2 x 5 using the scores data. The first five values belong to the first row
# of the matrix. Assign the result to the variable, scores.matrix, and display the result.
scores.matrix<-matrix(scores, nrow=2, ncol=5 , byrow = TRUE) #create scores matrix
scores.matrix

# g) Without hardcoding the value 5, show the code for displaying the first and last columns of the
# matrix.
scores.matrix.col <- ncol(scores.matrix) # we get the col value from the matrix
scores.matrix[,c(1, scores.matrix.col)] # first and last columns

# h) Assign row names for the scores.matrix as Student_1, Student_2,… and column names as
# Quiz_1, Quiz_2 …. The code should not hard code the values 2 and 5.
scores.matrix.row <- nrow(scores.matrix)
students <- paste("Student", seq(1,scores.matrix.row), sep="_") # create student_1 and student_2
quizzes <- paste("Quiz", seq(1,scores.matrix.col), sep="_")  # create Quiz_* names
dimnames(scores.matrix) <- list(students,quizzes)
scores.matrix

#Part 2) 

# a) Show the code for creating the data frame and display the resulting data frame. This is not an
# automated code. Create the values manually and then the data frame.

#I used csv as example but, I wrote the dataframe from scratch
#setwd("D:/studies/2017-fall/CS444/hw/CS544_HW1_Riesco/") #switch directory to be sure where the csv file is
getwd()
path <- file.path(getwd(),"weather.csv") # create the csv from the page and I load it 
weather.info.csv <- read.csv(file=path, header=TRUE, sep=",")
weather.info.csv

#this is the handmade dataframe from the table online
weather.info <- data.frame(Month = c("January",   "February",  "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ),
                           Monthly_Avg = c(4.7, 6.1, 12.8, 23.9, 35.5, 45.0, 49.1, 48.1, 41.6, 30.2, 20.7, 10.1),
                            DailyMax_Avg = c(13.6, 14.7, 20.7, 30.4, 41.3, 50.4, 54.1, 53.3, 47.1, 36.4, 28.1, 18.4),
                            DailyMin_Avg = c(-4.1, -2.4,  5.0, 17.4, 29.8, 39.5, 44.0, 43.0, 36.1, 24.0, 13.3,  1.7),
                            Record_High = c(48, 43, 54, 60, 66, 72, 71, 72, 69, 62, 52, 47),
                            Record_Low = c(-47, -46,-38, -20,  -2,   8,  24,  20,   9,  -5, -20,-46)
                            )

                             
weather.info # print dataframe

# b) Show the summary for Monthly_Avg, DailyMax_Avg, DailyMin_Avg, Record_High, and
# Record_Low.

summary(weather.info$Monthly_Avg)
summary(weather.info$DailyMax_Avg)
summary(weather.info$DailyMin_Avg)
summary(weather.info$Record_High)
summary(weather.info$Record_Low)
summary(weather.info)

# c) Show the data frame sliced using the columns Month, Record_High, and Record_Low.
weather.info[c("Month", "Record_High", "Record_Low")]


# d) Show the data frame sliced using the first and last row. Do not hard code 12 in the
# expression, i.e., the code should work for a data frame of any size.
weather.info[c(1, nrow(weather.info)), ]

#e) Show all rows of the data frame whose DailyMax_Avg is greater than 50.
subset(weather.info, DailyMax_Avg > 50 )
# f) Modify the data by adding a new column, Record_Deviation, showing the difference between
# the Record_High and Record_Low. Display the new resulting data frame.
Record_Deviation <- weather.info$Record_High - weather.info$Record_Low
weather.info$Record_Deviation <- Record_Deviation

weather.info # print dataframe with the new column


#REFERENCES 
#http://www.r-tutor.com/r-introduction/matrix
#https://www.tutorialspoint.com/r/r_mean_median_mode.htm
#http://rprogramming.net/read-csv-in-r/
# Version 1.0.153 – © 2009-2017 RStudio, Inc.
# Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/538.1 (KHTML, like Gecko) rstudio Safari/538.1 Qt/5.4.1


