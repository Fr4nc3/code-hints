# Text classification using a Naive Bayes scheme
# Data : 20 Newsgroups 
# Download link : http://www.cs.umb.edu/~smimarog/textmining/datasets/

# Load all the required libraries. Note : Packages need to be installed first.
library(dplyr)
library(caret)  
library(tm)
library(RTextTools)
library(doMC)
library(e1071)
registerDoMC(cores=detectCores())


# Load data. 
# We will use the 'train-all-terms' file which contains over 11300 messages.
# Read file as a dataframe
ng.df <- read.table("20ng-train-all-terms.txt", header=FALSE, sep="\t", quote="", stringsAsFactors=FALSE, col.names = c("topic", "text"))

# Preview the dataframe
# head(ng.df) # or use View(ng.df)



# How many messages do each of the 20 categories contain?
table(ng.df$topic)


# Read topic variable as a factor variable
ng.df$topic <- as.factor(ng.df$topic)

# Randomize : Shuffle rows randomly.
set.seed(2016)
ng.df <- ng.df[sample(nrow(ng.df)), ]
ng.df <- ng.df[sample(nrow(ng.df)), ]


# Create corpus of the entire text
corpus <- Corpus(VectorSource(ng.df$text))

# Total size of the corpus
length(corpus)

# Inspect the corpus
inspect(corpus[1:5])




# Tidy up the corpus using 'tm_map' function. Make the following transformations on the corpus : change to lower case, removing numbers, 
# punctuation and white space. We also eliminate common english stop words like "his", "our", "hadn't",  couldn't", etc using the
# stopwords() function.


# Use 'dplyr' package's excellent pipe utility to do this neatly
corpus.clean <- corpus %>%
  tm_map(content_transformer(tolower)) %>% 
  tm_map(removePunctuation) %>%
  tm_map(removeNumbers) %>%
  tm_map(removeWords, stopwords(kind="en")) %>%
  tm_map(stripWhitespace)


# Create document term matrix
dtm <- DocumentTermMatrix(corpus.clean)
dim(dtm)



# Create a 75:25 data partition. Note : 5000 (~50% of the entire set) messages were used for this analysis.

ng.df.train <- ng.df[1:8470,]
ng.df.test <- ng.df[8471:11293,]

dtm.train <- dtm[1:8470,]
dtm.test <- dtm[8471:11293,]

dim(dtm.test)

corpus.train <- corpus.clean[1:8470]
corpus.test <- corpus.clean[8471:11293]

# Find frequent words which appear five times or more

fivefreq <- findFreqTerms(dtm.train, 5)
length(fivefreq)

dim(dtm.train)



# Build dtm using fivefreq words only. Reduce number of features to length(fivefreq)
system.time( dtm.train.five <- DocumentTermMatrix(corpus.train, control = list(dictionary=fivefreq)) )



system.time( dtm.test.five <- DocumentTermMatrix(corpus.test, control = list(dictionary=fivefreq)) )

# converting word counts (0 or more) to presence or absense (yes or no) for each word
convert_count <- function(x) {
  y <- ifelse(x > 0, 1,0)
  y <- factor(y, levels=c(0,1), labels=c("No", "Yes"))
  y
}

# Apply yes/no function to get final training and testing dtms

system.time( ng.train <- apply(dtm.train.five, 2, convert_count) )

system.time ( ng.test <- apply(dtm.test.five, 2, convert_count) )



# Build the NB classifier
system.time (ngclassifier <- naiveBayes(ng.train, ng.df.train$topic))

# Make predictions on the test set
system.time( predictions <- predict(ngclassifier, newdata=ng.test) )
predictions

cm <- confusionMatrix(predictions, ng.df.test$topic )
cm