##########################################
# Francia Riesco Assignment 3
# 09/21/2017 (LAST HOMEWORK)
##########################################
##########################################
# Francia Riesco Assignment4
# 10/02/2017
##########################################
setwd("D:/studies/2017-fall/CS688/hw/")
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
Tags
set.seed(0)
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
########################################################################


# Part  4A
# For the newsgroup classification problem in Assignment 3, estimate 
# the effectiveness of your classification: 
#   .	Create the confusion matrix
# .	Clearly mark the values TP, TN, FP, FN 

TP<-sum(prob.test[1:100]==Tags[1:100])
FP<-sum(prob.test[1:100]!=Tags[1:100])
FN<-sum(prob.test[101:200]!=Tags[101:200])
TN<-sum(prob.test[101:200]==Tags[101:200])
table(prob.test,Tags)

# .	Calculate Precision
# .	Calculate Recall
# .	Calculate F-score
precision<-(TP/(TP+FP))*100
recall<-(TP/(TP+FN))*100
fscore<-(2*precision*recall)/(precision+recall)
precision
recall
fscore


doc <- c(Doc1.Train,Doc1.Test,Doc2.Train,Doc2.Test) 

corpus <- VCorpus(VectorSource(doc))
#tm::inspect(corpus)


corpus.temp <- tm_map(corpus.temp, stripWhitespace)
#convert to the lower case
#delete non-content-bearing words using a predefined stop word list.
corpus.temp <- tm_map(corpus.temp,removeWords,stopwords("english")) 
# Perform Stemming
corpus.temp <- tm_map(corpus.temp, stemDocument, language = "english")

dtm <-DocumentTermMatrix(corpus.temp) # Document term matrix
dtmImproved <- DocumentTermMatrix(corpus.temp, control=list(minWordLength = 2, minDocFreq=5))

tm::inspect(dtm)
tm::inspect(dtmImproved)


train.doc<-as.matrix(dtmImproved[c(1:100,201:300),])
test.doc<-as.matrix(dtmImproved[c(101:200,301:400),])

Tags <- factor(c(rep("Sci",100), rep("Rec",100))) # Tags - Correct answers for the training dataset
Tags
set.seed(0)

prob.test<- knn(train.doc, test.doc, Tags, k = 2, prob=TRUE) # k-number of neighbors considered


a <- 1:length(prob.test)
b <- levels(prob.test)[prob.test]
c <- attributes(prob.test)$prob
d <- as.vector(matrix(1,nrow=length(c))) # create a vector with 1 size of Prob
f <- c == d # compare two vectors

result <- data.frame(Doc=a, Predict=b,Prob=c, Correct=f)
result
sum(c)/length(Tags) # Overall probability

sum(prob.test==Tags)/length(Tags) # % Correct Classification



TP<-sum(prob.test[1:100]==Tags[1:100])
FP<-sum(prob.test[1:100]!=Tags[1:100])
FN<-sum(prob.test[101:200]!=Tags[101:200])
TN<-sum(prob.test[101:200]==Tags[101:200])
table(prob.test,Tags)


precision<-(TP/(TP+FP))*100
recall<-(TP/(TP+FN))*100
fscore<-(2*precision*recall)/(precision+recall)
precision
recall
fscore

#Forecast_kWh_Demand.R wih my moficications
library("RSNNS")
library("jsonlite")

### Pre-Process Data & Call Neural Network 
Parse.JSON.Input <- function (inputs) 
{
  ix <- grep("Relative_Humidity",inputs$historian$TagName); InputData <-data.frame(inputs$historian$Samples[[ix]]$TimeStamp,stringsAsFactors = FALSE); 
  InputData <-cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outdoor_Dewpoint",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outdoor_Temperature",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("BUE_Stud_Electric_Demand_kW",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Optimal_Electric_Demand_kW",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outputs.Predicted_Electric_Demand",inputs$parameters$Name); InputData <- cbind(InputData, inputs$parameters$Tag[[ix]],stringsAsFactors = FALSE)
  colnames(InputData) <- c("DATE","Relative_Humidity","Outdoor_Dewpoint","Outdoor_Temperature","Electric_Demand_kW","Optimal_Electric_Demand_kW","TagName")
  return (InputData) # Returned object
}

Forecast.Electric.Demand <- function (Raw_Data) 
{
  library("RSNNS")
  print("2. Inputs sent to function: Forecast.Electric.Demand()")
  # Convert Time Stemps
  Num.Data.Points <- dim(Raw_Data)[1]
  Time.Stamp <- strptime(Raw_Data$DATE,"%Y-%m-%dT%H:%M:%S")
  
  # Select Training Range 
  StartTime <- 1 # which(Time.Stamp=="2014-03-01 01:00:00 EST")
  TrainRange <- StartTime:Num.Data.Points
  print(paste0("Training data start date: ",Time.Stamp[StartTime]))
  
  # Extract Hours field from Time.Stamp
  Hours <- as.numeric(format(Time.Stamp,'%H')) # Replace this Line
  # Insert your code here
  Day.Date <- as.numeric(format(Time.Stamp,'%d'))   
  # Extract Days field from Time.Stamp
  Day.Number <- as.numeric(format(Time.Stamp, '%w'))# Replace this Line
  # Insert your code here
  Day.Number[Day.Number==0]=7
  Day.Name <- weekdays(Time.Stamp)
  # Modify Hours & Days
  temp <- 12-Hours; temp[temp>=0] = 0
  Hours.Modified <- Hours + 2*temp
  Day.Number.Modified <- Day.Number
  
  # Insert your code here
  Day.Number.Modified[Day.Number<6]=1
  Day.Number.Modified[Day.Number==6]=2
  
  print("Extracting Hour_of_Day & Day_of_Week fields from the DATE field Time Stamp ")
  
  # Choose Data to Process 
  Dependent.Ix <- c(2:4) # Select dependent columns
  Dependent.Data <- cbind(Hours.Modified, Day.Number.Modified, Raw_Data[TrainRange,Dependent.Ix]); # X ()
  Independent.Ix <- c(5) # Select Independent columns
  Independent.Data <- Raw_Data[TrainRange,Independent.Ix]; # Y (Actual Electric Demand )
  print("Dependent data tags: ");  print(names(Dependent.Data))
  print("Independent data tags: ");  print(names(Raw_Data[Independent.Ix]))
  
  # Define NuNet Inputs
  inputs <- Dependent.Data # Actual Consumption - used for training
  targets <- Independent.Data # Expected Consumption (Regression data) used as Tags
  Percent.To.Test <- 0.30 # Split the input data into train and test
  print("Define NuNet Inputs: "); print(paste0("Percent of input data to test: ", 100*Percent.To.Test, " %"))
  
  # Train NuNet & Get Predictions
  print("Train NuNet & Get Predictions, please wait... ");
  Predicted.Electric.Demand <- TrainNuNet(inputs,targets,Percent.To.Test) 
  # Predicted.Electric.Demand <- list(rep(0,Num.Data.Points)) # Populate with zero
  print("NuNet Training finished!");
  
  # Actual.Electric.Demand <- Independent.Data 
  # Output <- list(Predicted.Electric.Demand)
  Output <- data.frame("TimeStamp"=Time.Stamp,"Value"=unlist(Predicted.Electric.Demand),"Quality"=3)
  
  return (Output) # Returned object
  
}


TrainNuNet <- function (inputs,targets,Percent.To.Test) 
{
  # Normalize the Data 
  if (is.null(dim(inputs))) # Single Column Input
  {
    z <- max(inputs, na.rm=TRUE) # find Max in Single Input Column
    inputs.scale <- z; targets.scale <- max(targets)
    inputs.normalized <- inputs/inputs.scale # Normalize Data
    targets.normalized <- targets/targets.scale # Normalize Data 
  }
  else # Multi Colum Input
  {
    z <- apply(inputs, MARGIN = 2, function(x) max(x, na.rm=TRUE)) # find Max in Each Input Column
    inputs.scale <- as.vector(z); targets.scale <- max(targets);
    inputs.normalized <- sweep(inputs, 2, inputs.scale, `/`) # Normalize Data
    targets.normalized <- targets/targets.scale # Normalize Data   
  }
  
  
  # Split the Data into Train and Test
  patterns <- splitForTrainingAndTest(inputs.normalized, targets.normalized, ratio = Percent.To.Test) 
  set.seed(13);
  
  # Train NN to folow Actual 
  # The use of an Elman network (Elman 1990) for time series regression.
  model <- elman(patterns$inputsTrain, patterns$targetsTrain,
                 size = c(10, 10), learnFuncParams = c(0.1), maxit = 1300,
                 inputsTest = patterns$inputsTest, targetsTest = patterns$targetsTest,
                 linOut = FALSE)
  # model <- elman(patterns$inputsTrain, patterns$targetsTrain,
  #                size = c(8, 8), learnFuncParams = c(0.1), maxit = 500,
  #                inputsTest = patterns$inputsTest, targetsTest = patterns$targetsTest,
  #                linOut = FALSE)
  
  NN.fitted.Train <- model$fitted.values*targets.scale 
  NN.fitted.Test <- model$fittedTestValues*targets.scale 
  
  Predicted.Electric.Demand <- c(NN.fitted.Train,NN.fitted.Test)
  
  result <- list(Predicted.Electric.Demand)
  
  return (result) # Returned object
}

wrapper <- function(inputJSON.Data){
  # # Import data 
  
  inputs <- fromJSON(inputJSON.Data, flatten=TRUE)
  InputData <- Parse.JSON.Input(inputs) # Turn JSON Input to DataFrame
  print("1. Historian Database input tags imported to R Script:")
  print(names(InputData))
  Output <- Forecast.Electric.Demand(InputData) 
  temp <- as.character( Output$TimeStamp); Output$TimeStamp <- paste0(sub(" ","T",temp),"Z")
  
  # In Historian Format 
  z <- list("TagName"=InputData$TagName[1],ErrorCode=0,"DataType"="DoubleFloat" ,"Samples"=Output)
  
  Predicted.Electric.Demand <- toJSON(list(z),pretty=TRUE)
  print("3. Predicted Electric Demand from NuNet saved to Historian Database")
  
  return(Predicted.Electric.Demand)
}

# Example: Shiny app that search Wikipedia web pages
# File: server.R 
library(shiny)
library(tm)
library(stringi)
library(proxy)
library(wordcloud)
library(ggplot2)   
source("WikiSearch.R")

shinyServer(function(input, output) {
  output$distPlot <- renderPlot({ 
    
    # Progress Bar while executing function
    withProgress({
      setProgress(message = "Mining Wikipedia ...")
      result <- SearchWiki(input$select)
    })
    #result
    wf <- data.frame(word=names(result), freq=result)   
    wf<- head(wf,50)  
    #freq.fifty <- head(result,50)
    #plot(result, labels = input$select, sub = "",main="Wikipedia Search")
    #wordcloud(names(freq.fifty), freq.fifty, min.freq=5, colors=brewer.pal(6, "Dark2"))
    ggplot(subset(wf, freq>50), aes(x = reorder(word, -freq), y = freq)) +
      geom_bar(stat = "identity") + 
      theme(axis.text.x=element_text(angle=45, hjust=1))
  })
})

### --- Example 8: Search Wikipedia web pages. --------
# Save these 3 files separately in the same folder (Related to HW#4)
# Example: Shiny app that search Wikipedia web pages
# File: ui.R 
library(shiny)
titles <- c("Web_analytics","Text_mining","Integral", "Calculus", 
            "Lists_of_integrals", "Derivative","Alternating_series",
            "Pablo_Picasso","Vincent_van_Gogh","Lev_Tolstoj","Web_crawler")
# Define UI for application 
shinyUI(fluidPage(
  # Application title (Panel 1)
  titlePanel("Wiki Pages"), 
  # Widget (Panel 2) 
  sidebarLayout(
    sidebarPanel(h3("Search panel"),
                 # Where to search 
                 selectInput("select",
                             label = h5("Choose from the following Wiki Pages on"),
                             choices = titles,
                             selected = titles, multiple = TRUE),
                 # Start Search
                 submitButton("Results")
    ),
    # Display Panel (Panel 3)
    mainPanel(                   
      h1("Display Panel",align = "center"),
      plotOutput("distPlot")
    )
  )
))

# Wikipedia Search
# Mofified by friesco
library(tm)
library(stringi)
library(WikipediR)
# library(proxy)

SearchWiki <- function (titles) {
  wiki.URL <- "https://en.wikipedia.org/wiki/"
  articles <- lapply(titles,function(i) stri_flatten(readLines(stri_paste(wiki.URL,i)), col = " "))
  
  # articles <- lapply(titles,function(i) page_content("en","wikipedia", page_name = i,as_wikitext=TRUE)$parse$wikitext)
  
  docs <- VCorpus(VectorSource(articles)) # Get Web Pages' Corpus
  remove(articles)
  
  # Text analysis - Preprocessing 
  transform.words <- content_transformer(function(x, from, to) gsub(from, to, x))
  temp <- tm_map(docs, transform.words, "<.+?>", " ")
  temp <- tm_map(temp, transform.words, "\t", " ")
  temp <- tm_map(temp, content_transformer(tolower)) # Conversion to Lowercase
  temp <- tm_map(temp, PlainTextDocument)
  temp <- tm_map(temp, stripWhitespace)
  temp <- tm_map(temp, removeWords, stopwords("english"))
  temp <- tm_map(temp, removePunctuation)
  temp <- tm_map(temp, stemDocument, language = "english") # Perform Stemming
  remove(docs)
  
  # Create Dtm 
  dtm <- DocumentTermMatrix(temp)
  dtm <- removeSparseTerms(dtm, 0.4)
  dtm$dimnames$Docs <- titles
  docsdissim <- dist(as.matrix(dtm), method = "euclidean") # Distance Measure
  #h <- hclust(as.dist(docsdissim), method = "ward.D2") # Group Results
  
  freq <- sort(colSums(as.matrix(dtm)), decreasing=TRUE)   
  # h <- head(freq, 50)  
  h <- freq
  # max(freq) # Max appearance frequency of a term (84)
  # findFreqTerms(dtm,max.Freq,max(freq))
  # ord <- order(freq) # Ordering the frequencies (ord contains the indices))
  # freq[tail(ord)] # Most frequent terms & their frequency (most frequent term "the" appearing 85 times)
  # 
  # findFreqTerms(dtm, lowfreq=10) # List terms (alphabetically) with frequency higher than 10
  
}




