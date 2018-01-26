h <-list(2,4,6,8,10)
h[3]<-"a"
h[is.numeric()]
die()

A <- matrix(1:9, nrow=3,ncol=3) # Matrix A (3x3)
B <- matrix(rep(10,6), nrow=3,ncol=2) # Matrix B (3x2)
B*B # Element wise multiplication
A%*% B # Matrix multiplication
a <- matrix(1:3,nrow=3,ncol=1) # Row Vector a
t(a)%*%B # Vector a is transposed first

library(XML)

SearchQuery <- "FRONTLINE LTD"
HTML.dataset <- paste0("http://www.sec.gov/cgi-bin/browse-edgar?company=", SearchQuery,"&owner=exclude&action=getcompany")

# Function to strip the table data from the HTML files
sieve.HTML <- function(URL) {
  table <- readHTMLTable(URL) # Read HTML table into a list
}

temp.HTML.text <- lapply(HTML.dataset,function(x) sieve.HTML(x)) # 

Tab.Names <- names(temp.HTML.text[[1]][[3]]) # Tab Names in the HTML
# [1] "Filings"          "Format"           "Description"      "Filed/Effective"  "File/Film Number"
query <- "Interactive Data" # To search for
temp<-grep(query, temp.HTML.text[[1]][[3]]$Format)
Filings.Number <- temp.HTML.text[[1]][[3]]$"Filings"[temp] # Filings Number
Effective.Dates <- temp.HTML.text[[1]][[3]]$"Filed/Effective"[temp] # Effective File Dates 
File.Number <- temp.HTML.text[[1]][[3]]$"File/Film Number"[temp] # File Number 

query <- "Report of foreign issuer"
temp<-grep(query, temp.HTML.text[[1]][[3]]$Description)





# library(tm)
# doc1 <- c("Web Analytics", "Text Analysis", "Web Mining", "Text Mining")
# doc2 <- c("Data Processing", "Machine Learning", "learn from data", "Big Data")
# doc3 <- c("bedroom furniture", "dining room furniture", "diner chair", "new chairs")
# doc <- c(doc1,doc2,doc3) # Merge all terms from all the Documents
# source <-Corpus(VectorSource(doc))
# tm::inspect(source)
# dtm <- as.matrix(DocumentTermMatrix(Corpus(VectorSource(doc)))) # Document term matrix
# 
# 
# foldersTrain <- list.dirs(pathTrain, full.names = FALSE)
# foldersTest <- list.dirs(pathTest, full.names = FALSE)
# #folders
# trainCorpuses <- list()
# testCorpuses <-list()

# for (i in 1:length(foldersTrain)) {
#   if(foldersTrain[i]!=""){ # skip root folder
#     print (foldersTrain[i])
#     Temp1 <- DirSource(file.path(pathTrain,foldersTrain[i]))
#     #load in a list of corpuses the first 100 files
#     trainCorpuses[i] <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
#     #rm(Temp1)
#   }
# }
# for (i in 1:length(foldersTest)) {
#   if(foldersTest[i]!=""){ # skip root folder
#     print (foldersTest[i])
#     Temp1 <- DirSource(file.path(pathTrain,foldersTest[i]))
#     #load in a list of corpuses the first 100 files
#     testCorpuses[i] <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
#     #rm(Temp1)
#   }
# }
library(Rcrawler)

Rcrawler(Website = "http://www.glofile.com", no_cores = 4, no_conn = 4)