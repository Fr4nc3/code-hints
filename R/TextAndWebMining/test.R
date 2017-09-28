 library(tm)
 doc1 <- c("Web Analytics", "Text Analysis", "Web Mining", "Text Mining")
 doc2 <- c("Data Processing", "Machine Learning", "learn from data", "Big Data")
 doc3 <- c("bedroom furniture", "dining room furniture", "diner chair", "new chairs")
 doc <- c(doc1,doc2,doc3) # Merge all terms from all the Documents
 source <-Corpus(VectorSource(doc))
 tm::inspect(source)
 dtm <- as.matrix(DocumentTermMatrix(Corpus(VectorSource(doc)))) # Document term matrix


 foldersTrain <- list.dirs(pathTrain, full.names = FALSE)
 foldersTest <- list.dirs(pathTest, full.names = FALSE)
 folders
 trainCorpuses <- list()
 testCorpuses <-list()

 for (i in 1:length(foldersTrain)) {
   if(foldersTrain[i]!=""){  #skip root folder
     print (foldersTrain[i])
     Temp1 <- DirSource(file.path(pathTrain,foldersTrain[i]))
    # load in a list of corpuses the first 100 files
     trainCorpuses[i] <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
     rm(Temp1)
   }
 }
 for (i in 1:length(foldersTest)) {
   if(foldersTest[i]!=""){  #skip root folder
     print (foldersTest[i])
     Temp1 <- DirSource(file.path(pathTrain,foldersTest[i]))
   #  load in a list of corpuses the first 100 files
     testCorpuses[i] <- Corpus(URISource(Temp1$filelist[1:100]),readerControl=list(reader=readPlain))
     rm(Temp1)
   }
 }
library(Rcrawler)

Rcrawler(Website = "http://www.glofile.com", no_cores = 4, no_conn = 4)