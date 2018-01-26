# Wikipedia Search
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