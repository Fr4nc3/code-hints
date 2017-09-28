##########################################
# Fr4nc3
# 09/21/2017
##########################################
setwd("D:/studies/e/")
getwd()
### --- From the Module 3  ----
library(tm) # Framework for text mining.
library(SnowballC) # Provides wordStem() for stemming.
library(qdap) # Quantitative discourse analysis of transcripts.
library(qdapDictionaries)
library(dplyr) # Data preparation and pipes %>%.
library(RColorBrewer) # Generate palette of colors for plots.
library(ggplot2) # Plot word frequencies.
library(scales) # Common data analysis activities.
# Text Classification
library(class) # Using kNN 

#D:\studies\2017-fall\CS688\hw\hw3\20Newsgroups\20news-bydate-train

pathTrain <- file.path(getwd(),"20Newsgroups", "20news-bydate-train")
pathTest <- file.path(getwd(),"20Newsgroups", "20news-bydate-test")
pathTrain

#a) For each subject select: 
Temp1 <- DirSource(file.path(pathTrain,"sci.space/") )
#load 100 train documents
Doc1.Train <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
Temp1 <- DirSource(file.path(pathTest,"sci.space/") )
Doc1.Test <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
Temp1 <- DirSource(file.path(pathTrain,"rec.autos/") )
Doc2.Train <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
Temp1 <- DirSource(file.path(pathTest,"rec.autos/") )
Doc2.Test <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
#tm::inspect(Doc1.Train)

#b)	Obtain the merged Corpus (of 400 documents), please keep the order as 
doc <- c(Doc1.Train,Doc1.Test,Doc2.Train,Doc2.Test) 

corpus <- VCorpus(VectorSource(doc))
#tm::inspect(corpus)

# c)	Implement preprocessing (clearly indicate what you have used)
corpus.temp <- tm_map(corpus, removePunctuation) # Remove Punctuation
corpus.temp <- tm_map(corpus.temp, stripWhitespace)
#convert to the lower case
corpus.temp <- tm_map(corpus.temp, content_transformer(tolower))
#remove punctuation
corpus.temp <- tm_map(corpus.temp, removePunctuation) 
#remove numbers
corpus.temp <- tm_map(corpus.temp, removeNumbers) 
#delete non-content-bearing words using a predefined stop word list.
corpus.temp <- tm_map(corpus.temp,removeWords,stopwords("english")) 
# Perform Stemming
corpus.temp <- tm_map(corpus.temp, stemDocument, language = "english")


# d)	Create the Document-Term Matrix using the following arguments
dtm <-DocumentTermMatrix(corpus.temp) # Document term matrix
dtmImproved <- DocumentTermMatrix(corpus.temp, control=list(minWordLength = 2, minDocFreq=5))

tm::inspect(dtm)
tm::inspect(dtmImproved)


#e)	Split the Document-Term Matrix into 
train.doc<-as.matrix(dtmImproved[c(1:100,201:300),])
test.doc<-as.matrix(dtmImproved[c(101:200,301:400),])
#trainMatrix

#f)	Use the abbreviations "Sci" and "Rec" as tag factors in your classification. 
Tags <- factor(c(rep("Sci",100), rep("Rec",100))) # Tags - Correct answers for the training dataset
Tag

#g)	Classify text using the kNN() function
prob.test<- knn(train.doc, test.doc, Tags, k = 2, prob=TRUE) # k-number of neighbors considered

# Display Classification Results
#h)	Display classification results as a R dataframe and name the columns as: 
a <- 1:length(prob.test)
b <- levels(prob.test)[prob.test]
c <- attributes(prob.test)$prob
d <- as.vector(matrix(1,nrow=length(c))) # create a vector with 1 size of Prob
f <- c == d # compare two vectors

result <- data.frame(Doc=a, Predict=b,Prob=c, Correct=f)
result
sum(c)/length(Tags) # Overall probability

#i)	What is percentage of correct (TRUE) classifications? 
sum(prob.test==Tags)/length(Tags) # % Correct Classification

