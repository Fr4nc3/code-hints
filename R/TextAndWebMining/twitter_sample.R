#####################################
# TWITTER
# October 8th, 2017
####################################
library(twitteR)
library(wordcloud)
library(ggplot2)  
library(tm)
library(SnowballC)
setwd("path")

# Consumer Key (API Key)	etgyiTRo4tqWUeo6N7Vmjw1OR
# Consumer Secret (API Secret)	x8Pzl8d1hbRoyzX7YzpFFdePBIjNxYE9LRVkuvl18zQ1GuXTgp
# Access Token	96573557-fPKXh6oGRzpLXOHNubf8EBBPOmnaDuUQwgaHK0WvG
# Access Token Secret	zj8iHqcljprAsASS8fiN8mmNfmesPqDm4wa58jCEZ37nj

# Use your own Twitter Developer API Key and Secret
consumer_key <- ""
consumer_secret <-""
access_token <- ""
access_secret <- ""

setup_twitter_oauth(consumer_key, consumer_secret, access_token, access_secret)
country1 <- "@fr4nc3"
country2 <- "@cnn"
# a)	Pick two of your favorite states in US (or two countries) and search for the tweets associated with these two terms.
tweets.country1 <- searchTwitter(country1, n = 500)
tweets.country2 <- searchTwitter(country2, n = 500)
# b)	Create two separate data corpus for the above two sets of tweets.
tweets.country1.text <- lapply(tweets.country1, function(t) {t$getText()})
tweets.country2.text <- lapply(tweets.country2, function(t) {t$getText()})


data.country1.source <- VectorSource(tweets.country1.text)
data.country1.corpus <- VCorpus(data.country1.source )

data.country2.source <- VectorSource(tweets.country2.text)
data.country2.corpus <- VCorpus(data.country2.source )

# c)	Use the pre-processing transformations described in the lecture.
removeNumberWords <- function(x) {
  gsub("([[:digit:]]+)([[:alnum:]])*", "", x)
}
removeURL <- function(x) {
  gsub("(http[^ ]*)", "", x)
}

english.stopwords <- stopwords("en")
head(english.stopwords)

data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(removeURL))
data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(removePunctuation))
data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(removeWords),english.stopwords)
data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(removeNumberWords))
data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(stemDocument))
data.country1.corpus <- tm_map(data.country1.corpus, content_transformer(stripWhitespace))

data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(removeURL))
data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(removePunctuation))
data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(removeWords),english.stopwords)
data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(removeNumberWords))
data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(stemDocument))
data.country2.corpus <- tm_map(data.country2.corpus, content_transformer(stripWhitespace))


# d)	Create the term-document matrix for each state/country.
country1.tdm <- TermDocumentMatrix(data.country1.corpus)
country1.m <- as.matrix(country1.tdm)
country2.tdm <- TermDocumentMatrix(data.country2.corpus)
country2.m <- as.matrix(country2.tdm)
# e)	Compare the frequent terms from each state/country.
country1.wordFreq <- rowSums(country1.m)
country1.wordFreq <- sort(country1.wordFreq, decreasing=TRUE)

country2.wordFreq <- rowSums(country2.m)
country2.wordFreq <- sort(country2.wordFreq, decreasing=TRUE)

country1.wf<- head(country1.wordFreq,50) # 50 more popular
country2.wf<- head(country2.wordFreq,50) 

barplot(country1.wf,ylab="Frequency",xlab=paste("Frequent Words of ", country1, sep=" "), col="green")
barplot(country2.wf,ylab="Frequency",xlab=paste("Frequent Words of ", country2, sep=" "), col="blue")

# f)	Show word cloud for each state/country.
wordcloud(names(country1.wf), country1.wf, min.freq=5, colors=brewer.pal(8, "Dark2"), )
wordcloud(names(country2.wf), country2.wf, min.freq=5, colors=brewer.pal(8, "Dark2"))

# g)	Using the positive and negative word lists, compute the sentiment score (as described in the lecture) for all the tweets for each state/country. Draw your inference.
set.seed(137)

sentiment <- function(text, pos.words, neg.words) {
  text <- gsub('[[:punct:]]', '', text)
  text <- gsub('[[:cntrl:]]', '', text)
  text <- gsub('\\d+', '', text)
  text <- tolower(text)
  # split the text into a vector of words
  words <- strsplit(text, '\\s+')
  words <- unlist(words)
  # find which words are positive
  pos.matches <- match(words, pos.words)
  pos.matches <- !is.na(pos.matches)
  # find which words are negative
  neg.matches <- match(words, neg.words)
  neg.matches <- !is.na(neg.matches)
  # calculate the sentiment score
  score <- sum(pos.matches) - sum(neg.matches)
  cat (" Positive: ", words[pos.matches], "\n")
  cat (" Negative: ", words[neg.matches], "\n")
  return (score)
}

# Lexicons
pos.words = scan('positive-words.txt', what='character', comment.char=';')
neg.words = scan('negative-words.txt',  what='character', comment.char=';')

sentiment(names(country1.wordFreq),pos.words,neg.words)
sentiment(names(country1.wordFreq),pos.words,neg.words)

country1.scores <- sapply(tweets.country1.text,  sentiment, pos.words, neg.words)
barplot(table(country1.scores),  xlab=paste("Score", country1, sep=" "), ylab="Count", col="cyan")

country2.scores <- sapply(tweets.country2.text,  sentiment, pos.words, neg.words)
barplot(table(country2.scores),  xlab=paste("Score", country2, sep=" "), ylab="Count", col="yellow")








