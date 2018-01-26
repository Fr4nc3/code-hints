# Module 5 - Facebook

#### Section 3.2

library(Rfacebook)

# Use your credentials Old Way
fb.app.id <- "XXXXXX" # Your Credentials 
fb.app.secret <- "XXXXXX" # Your Credentials 
fb.oauth <- fbOAuth(app_id = fb.app.id, app_secret = fb.app.secret, extended_permissions = TRUE)

# To Get temporary access token, and use it instead
# Go to https://developers.facebook.com/tools/explorer & Click "Get Token"
fb.oauth <- "YYYYYYYYYY"
save(fb.oauth, file="facebook_credentials.YOURS") # Save Your Credentials for Everyday Use

## For temporary access, use the following
load(file="facebook_credentials.YOURS")


#### Section 3.3
library(devtools)
install_github("pablobarbera/Rfacebook/Rfacebook")
user <- getUsers("me", token = fb.oauth) 

user$id
user$name
user$first_name
user$last_name
user$gender
user$locale

library(RCurl)
library(RJSONIO)


# Latest Rfacebook Package Verion 
getFacebookId <- function (name) {
  data <- getUsers(name, token = fb.oauth)
  return (data['id'])
}

getFacebookId("donaldtrump")
getFacebookId("BUonline")


id1 <- getFacebookId("CNN")
id2 <- getFacebookId("BUonline")
users <- getUsers(c(id1, id2), token = fb.oauth)


users$id
users$name
users$likes
users$category

#### Section 3.4

# List of posts from a Facebook page

page <- getPage("BUonline", n=100, token=fb.oauth) 

# Show details about the first post
first.post <- page[1,]

first.post$message
first.post$likes_count
first.post$comments_count
first.post$shares_count
first.post$from_id
first.post$from_name
first.post$created_time
first.post$type
first.post$id

table(page$type)

# Most liked post
most.liked <- page[which.max(page$likes_count), ]

most.liked$message
most.liked$likes_count
most.liked$comments_count
most.liked$shares_count
most.liked$created_time
most.liked$type

# Most commented post

most.commented <- page[which.max(page$comments_count), ]

most.commented$message
most.commented$likes_count
most.commented$comments_count
most.commented$shares_count
most.commented$created_time
most.commented$type

# Most shared post

most.shared <- page[which.max(page$shares_count), ]

most.shared$message
most.shared$likes_count
most.shared$comments_count
most.shared$shares_count
most.shared$created_time
most.shared$type

# Get subset of posts

page <- getPage("BUonline", n=100, token=fb.oauth,
                since = '2014/12/01')

page <- getPage("BUonline", n=1000, token=fb.oauth,
                since = '2014/01/01', 
                until = '2014/12/31')


#### Section 3.5

page <- getPage("CNN", n=1000, token=fb.oauth,
                since = '2015/02/01', 
                until = '2015/02/28')

save(page, file = "cnn_posts.RData")

load(file = "cnn_posts.RData")

most.liked <- page[which.max(page$likes_count), ]
most.liked$id
most.liked$likes_count
most.liked$message

post <- getPost(most.liked$id, n.likes=1000,
                token=fb.oauth,  comments=FALSE)

# List of people that liked

likes <- post$likes
head(likes, n = 2)

# Information about the liked users

users <- getUsers(likes$from_id, token=fb.oauth)

# Common first names

first.names <- sort(
  table(users$first_name),
  decreasing=TRUE)

head(first.names, n = 5)

# Common last names

last.names <- sort(
  table(users$last_name),
  decreasing=TRUE)

head(last.names, n = 5)

#### Section 3.6

pages <- searchPages(string = "boston", n = 500, 
                     token = fb.oauth)

save(pages, file = "boston_pages.RData")

load(file="boston_pages.RData")

categories <- sort(
  table(pages$category),
  decreasing = TRUE)
head(categories, n = 5)

#### Section 3.7

library(XML)
# library(RCurl)
library(stringr)
# library(RSelenium)

# curl <- getCurlHandle()
# curlSetOpt(.opts = list(proxy = "http://24.91.118.38:8080"), curl = curl)
# ans <- getURL('http://www.cnn.com', curl = curl)
# opts <- list(proxy = "http://24.91.118.38", proxyusername = "tumbledown", 
#              proxypassword = "mypassword",proxyport = 36716)
# getURL("http://stackoverflow.com", .opts = opts)
# webpage <- getURL("http://govsm.com/w/House")
# webpage <- getURL("http://www.govsm.com/w/CAAssembly")

URL <- c("http://www.govsm.com/w/CAAssembly")
doc.html = htmlTreeParse(URL,useInternal = TRUE)
doc.text = unlist(xpathApply(doc.html, '//p', xmlValue))

assembly <- readHTMLTable(doc.html, which=1)
# webpage <- readHTMLTable(URL,as.data.frame = TRUE)
# assembly <- do.call(rbind.data.frame, webpage) # DataFrame
# assembly <- webpage[[1]] # DataFrame
# assembly <- assembly[-1,] # Remove first row

# assembly <- readHTMLTable(webpage, which=1)
names(assembly) <- str_trim(names(assembly))

names(assembly)

assembly[1:5, 
      c("First", "Last", "Party", 
        "District", "Facebook")]


getNodeValue <- function (node) {
  children <- xmlChildren(node)
  if (length(children) == 1)
    return (xmlValue(node))
  else {
    nodes <- children$a
    val <- xmlValue(nodes)
    if (val == "") {
      attr <- xmlAttrs(nodes)['href']
      return (toString(attr))
    } else {
      return (val)
    }
  }
}

assembly <- readHTMLTable(doc.html, which=1, elFun=getNodeValue)
names(assembly) <- str_trim(names(assembly))

assembly[1:3, 
      c("First", "Last", "Party", 
        "District", "Facebook")]

assembly$State <- substring(assembly$District, 1, 2)
assembly[1:10, 
      c("First", "Last", "Party", 
        "District", "State")]

fb.links <- assembly[(assembly$State %in% c("MA")), "Facebook"]
fb.links

fb.accounts <- 
  sapply(fb.links,
         function (x) {
           index <- regexpr("\\/[^\\/]*$", x)[1]
           substring(x, index + 1)
         }
  )

fb.accounts

# Download all facebook pages
fb.data <- NULL

for (account in fb.accounts){
  cat("\nDownloading for ", account, "\n")
  
  error <- tryCatch(
    df <- getPage(account, token=fb.oauth, n=1000, 
                  since='2014/01/01'),
    error = function(e) print(e)
  )
  if (inherits(error, 'error')){ next }
  
  # convert newlines to spaces for each message
  df$message <- gsub("\n", " ", df$message)
  
  # Filter posts with no messages
  df <- df[!is.na(df$message) & df$message!="",]
  
  # Add this data frame to the data
  fb.data <- rbind(fb.data, df)
}

nrow(fb.data)

save(fb.data, file="assembly_fb.RData")

load(file="assembly_fb.RData")

####
library(tm)
library(stringr)

# clean the text
clean_text <- function(message){
  
  # cleaning text
  text <- iconv(message, "latin1", "ASCII", sub="")
  
  text <- removePunctuation(
    removeNumbers(
      tolower(text)))
  
  removeURL <- function(x) {
    gsub("(http[^ ]*)", "", x)
  }
  text <- removeURL(text)
  text <- str_trim(text)
  return(text)
}

fb.data$text <- clean_text(fb.data$message)
nrow(fb.data)

# Filter data with text size > 100
fb.data <- fb.data[str_length(fb.data$text) > 100, ]
nrow(fb.data)

####

data.source <- VectorSource(fb.data$text)
data.corpus <- Corpus(data.source)

# transformations
stopwords.1 <- stopwords("en")
stopwords.2 <- c("american", "americans", "can",       
                 "congress", "congressman", "get", 
                 "great", "assembly", "like", "make", 
                 "must", "new", "one", "said", "sen", 
                 "senate", "think", "today", "will")

stopwords <- c(stopwords.1, stopwords.2)

data.corpus <- 
  tm_map(data.corpus,
         content_transformer(removeWords),
         stopwords)

data.corpus <- 
  tm_map(data.corpus,
         content_transformer(stripWhitespace))

# inspect the first two values
inspect(data.corpus[1:2])

save(list=("data.corpus"),
     file = "assemblyDataCorpus.RData")

load(file="assemblyDataCorpus.RData")

# Build the term document matrix

tdm <- TermDocumentMatrix(data.corpus)

save(list=("tdm"),
     file = "assemblyTDM.RData")

load(file="assemblyTDM.RData")

# convert TDM to a matrix
m <- as.matrix(tdm)

# calculate the frequency of words 
wordFreq <- rowSums(m)

# Sort the words by descending order of frequency
wordFreq <- sort(wordFreq, decreasing=TRUE)

# Examine the top ten words
cbind(wordFreq[1:10])

# frequent terms
findFreqTerms(tdm, lowfreq=200)

# associations
findAssocs(tdm, "program", 0.5) 

# word cloud

library(wordcloud)

palette <- brewer.pal(8,"Dark2")
palette

set.seed(137)
wordcloud(words=names(wordFreq), 
          freq=wordFreq, 
          min.freq=200, 
          random.order=F,
          colors=palette)

set.seed(137)
wordcloud(words=names(wordFreq), 
          freq=wordFreq, 
          min.freq=150, 
          random.order=F,
          colors=palette)

#####




