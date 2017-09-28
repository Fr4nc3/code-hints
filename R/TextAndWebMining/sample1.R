#### sample code 

### --- Example 1: Convert to text single pdf files that is contained in a single folder. ----
exe.loc <- Sys.which("pdftotext") # location of "pdftotext.exe"
pdf.loc=file.path(getwd(),"PDF Files") # folder "PDF Files" with PDFs
myPDFfiles <- normalizePath(list.files(path = pdf.loc, pattern = "pdf",  full.names = TRUE)) # Get the path (chr-vector) of PDF file names

# Convert single pdf file to text by placing "" around the chr-vector of PDF file name
system(paste(exe.loc, paste0('"', myPDFfiles[1], '"')), wait=FALSE)

# Convert to text several pdf files that are contained in a single folder.
# Use lapply with in line function to convert each PDF file indexed by "i" into a text file 
lapply(myPDFfiles, function(i) system(paste(exe.loc, paste0('"', i, '"')), wait = FALSE))

### --- Example 2: The recommended data analysis packages (install if needed) include: ----
library(tm) # Framework for text mining.
library(SnowballC) # Provides wordStem() for stemming.
library(qdap) # Quantitative discourse analysis of transcripts.
library(qdapDictionaries)
library(dplyr) # Data preparation and pipes %>%.
library(RColorBrewer) # Generate palette of colors for plots.
library(ggplot2) # Plot word frequencies.
library(scales) # Common data analysis activities.
library(Rgraphviz) # Correlation plots.

### --- Example 2a: Extracting text content from text files and load them as Corpus. ----
loremipsum <- system.file("texts", "loremipsum.txt", package = "tm") # Path to "loremipsum.txt"
ovid <- system.file("texts", "txt", "ovid_1.txt", package = "tm") # Path to "ovid.txt"
Docs.pth <- URISource(sprintf("file://%s", c(loremipsum, ovid))) # Specify Source
corpus.txt<-VCorpus(Docs.pth) # load them as Corpus 
inspect(corpus.txt) 

corpus.txt[[2]]$content[1:3] # Examine the first 3 lines of the "ovid.txt" corpus 

### --- Example 2b: Extracting file content from a PDF file and load them as Corpus. ----
pdf.loc <- system.file(file.path("doc", "tm.pdf"), package = "tm") # Find the path to "tm.pdf"
pdf <- readPDF(control = list(text = "-layout"))(elem = list(uri = pdf.loc),
                                                 language = "en",
                                                 id = "id1")
cname<- URISource(pdf.loc) 
corpus.pdf <- Corpus(cname, readerControl=list(reader=readPDF))
inspect(corpus.pdf) 

pdf$content[1:10] # The first 10 lines of lis element "content"
pdf$meta # List "meta" 
corpus.pdf[[1]]$content 
corpus.pdf[[1]]$meta

### --- Example 3: Processing - Transforming the Corpus  ----

getTransformations() # The basic transforms available within tm package 

# Apply the function "tm_map()" and content_transformer() to the corpus
docs.tranf <- tm_map( corpus.txt, content_transformer(tolower)) # Conversion to Lowercase
corpus.txt[[2]]$content[1:3] # Original corpus with Uppercase
docs.tranf[[2]]$content[1:3] # Transformed Corpus all Lowercase

# Transforms the "@" into " ".
email.texts <- c("Jon_Smith@bu.edu",
                 "Subject: Speaker's Info", 
                 "I hope you enjoyed the lectures.",
                 "Here is address of the lecturer: ", "123 Main St. #25","Boston MA 02155") 
# Step 1: Create corpus
corpus.txt <- Corpus(DataframeSource(data.frame(email.texts)))
# Step 2: "content transformer()" crate a function to achieve the transformation
transform.chr <- content_transformer(function(x, pattern) gsub(pattern, " ", x))
docs.tranf <- tm_map(corpus.txt, transform.chr, "@")

corpus.txt[[1]]$content[1] # "Jon_Smith@bu.edu"
docs.tranf[[1]]$content[1] # "Jon_Smith bu.edu"

### --- Example 4: Replacing a word with another one  ----
transform.wors <- content_transformer(function(x, from, to) gsub(from, to, x))
docs.tranf <- tm_map(corpus.txt, transform.wors, "Jon_Smith", "Jane_Doe")

corpus.txt[[1]]$content[1] # "Jon_Smith@bu.edu"
docs.tranf[[1]]$content[1] # "Jane_Doe@bu.edu" 

library(SnowballC) # Stemming 
docs.tranf <- tm_map(corpus.txt, stemDocument) # Stemm original corpus

corpus.txt[[2]]$content[1] # "Subject: Speaker's Info"
docs.tranf[[2]]$content[1] # "Subject: Speaker Info"

  

### --- Example 5: Creating a Document Term Matrix  ----
Docs.pth <- system.file(file.path("doc", "tm.pdf"), package = "tm") # Path to tm.pdf
Docs.corpus <- Corpus(URISource(Docs.pth),readerControl = list(reader = readPDF(engine = "xpdf")))
dtm <- DocumentTermMatrix(Docs.corpus) # Document Term Matrix
freq <- colSums(as.matrix(dtm)) # Term frequencies
max(freq) # Max appearance frequency of a term (84)
findFreqTerms(dtm,max.Freq,max(freq)) # Find the term with max appearance ("the")
ord <- order(freq) # Ordering the frequencies (ord contains the indices))
freq[tail(ord)] # Most frequent terms & their frequency (most frequent term "the" appearing 85 times)
# with    for    and corpus   text    the 
# 17     22     23     25     26     85 

findFreqTerms(dtm, lowfreq=10) # List terms (alphabetically) with frequency higher than 10
# "and"       "are"       "can"       "corpus"    "documents" "for"   "metadata"  "mining"    "terms"     "text"      "the"       "this"      "which"     "with" 
findFreqTerms(dtm, lowfreq=17) # List terms (alphabetically) with frequency higher than 17
# "and"    "can"    "corpus" "for"    "text"   "the"    "with" 

# Create a Word Cloud Plot
library(wordcloud)
set.seed(123)
wordcloud(names(freq), freq, min.freq=5, colors=brewer.pal(6, "Dark2"))

matdtm <- as.matrix(dtm) # Convert dtm to a matrix
write.csv(matdtm, file=" dtm.csv") # Save matrix as CSV file

### --- Example 6: Creating a Matrix  ----
A <- matrix(1:9, nrow=3,ncol=3) # Matrix A (3x3)
B <- matrix(rep(10,6), nrow=3,ncol=2) # Matrix B (3x2)
B*B # Element wise multiplication
A%*% B # Matrix multiplication
a <- matrix(1:3,nrow=3,ncol=1) # Row Vector a
t(a)%*%B # Vector a is transposed first

### --- Example 7: String Operations   ----
unlist(strsplit("a.b.c", "\\.")) # Split the elements of a character vector 
# "a" "b" "c"

library(tau) # Using tau package 
tokenize("abc defghk")
# "abc"    " "      "defghk"

nchar("Web Analytics") # Counting the number of characters in a string

# Detecting a pattern in a string.
library(stringr) # Using stringr package
string1 <- "Web Analytics"
string2 <- "Data Analytics"
str_detect(string1, "Analytics") # "TRUE"
str_detect(string2, " Web") # "FALSE" 

# Date Strings Manipulations
string1 <- "12 may 2014"
string2 <- "1 may 2014"
regexp <- "([[:digit:]]{2}) ([[:alpha:]]+) ([[:digit:]]{4})" # define Date pattern to have 2 Day digits, text as Month, 4 digit Year
str_detect(string1, regexp) # "TRUE" - Using stringr package function "str_detect"
grepl(pattern = regexp, x = string1) # "TRUE" - Using base R package function "grepl"
grepl(pattern = regexp, x = string2) # "FALSE" - the day in the regexp was defined to have 2 digits

### --- Example 8: Fuzzy String Matching   ----
# Using The Jaccard measure
library(stringdist)
dict1 <- "analytics"
dict2 <- "analysis"
query <- "analisis"
A <- unlist(strsplit(dict1,"")) # Get the set of characters in dict1
B <- unlist(strsplit(dict2,"")) # Get the set of characters in dict2
Q <-  unlist(strsplit(query,"")) # Get the set of characters in query

UA <- union(A,Q)
IA <- intersect(A,Q) 
JA <- length(IA)/length(UA) # The Jaccard measure
sprintf("%s %f","The Jaccard Q-A measure is",JA) # Display calculated measure
# "The Jaccard Q-A measure is 0.625000"

UB <- union(B,Q)
IB <- intersect(B,Q) 
JB <- length(IB)/length(UB) # The Jaccard measure
sprintf("%s %f","The Jaccard Q-B measure is",JB) # Display calculated measure
# "The Jaccard Q-B measure is 0.833333"

### --- Example 9: Document Clustering by Most Frequent Strings   ----
# Assume that you have several (3) documents with few most frequent strings in them and you would like to group them together by similarity. 
library(tm)
doc1 <- c("Web Analytics", "Text Analysis", "Web Mining", "Text Mining")
doc2 <- c("Data Processing", "Machine Learning", "learn from data", "Big Data")
doc3 <- c("bedroom furniture", "dining room furniture", "diner chair", "new chairs")
doc <- c(doc1,doc2,doc3) # Merge all terms from all the Documents

dtm <- as.matrix(DocumentTermMatrix(Corpus(VectorSource(doc)))) # Document term matrix

colnames(dtm) # Gives All of the terms contained in the document term matrix

# Using Jaccard Distance to find distance between terms and corresponding documents
library(arules) # Load similarity measures package
d <- dist(dtm, method="binary") # Find distance between terms in dtm
cl <- hclust(as.dist(d)) # Perform clustering
cl$labels=doc # Assign labels (terms used) to cluster leaves
plot(cl,main="Jaccard Distance") # Set plot title


# With stemmed terms 
corpus.temp <- tm_map(Corpus(VectorSource(doc)), stemDocument, language = "english")
dtm <- as.matrix(DocumentTermMatrix(corpus.temp))
d <- dist(dtm, method="binary") # Find distance between terms in dtm
cl <- hclust(as.dist(d)) # Perform clustering
cl$labels=doc # Assign labels (terms used) to cluster leaves
plot(cl,main="Jaccard Distance with Stemming") # Set plot title


# Hierarchical clustering
library(stringdist)
d <- stringdistmatrix(doc, doc) # Pairwise string distances (optimal string alignment)
cl <- hclust(as.dist(d)) # Perform hierarchical clustering
cl$labels=doc # Assign labels to cluster leaves
plot(cl)

### --- Example 10: Document kNN Text Classification   ----
library("tm")
Doc1 <- "I spent 10K on my car. Compared to the prices of most cars in their class it was cheap. It is a red car so I like it and it has a lot of space."
Doc2 <- "I checked the car prices and I could not find a red car for under 10K. So the price was good even though it had a hole. I heard that it belonged to a movie star." 
Doc3 <- "I like the red color, so I would buy a red car even if the car's price is over 10K."
Doc4 <- "I don't like red cars. The insurance for red cars is higher regardless of the price and I would not spend more than 10K. I like black cars."
Doc5 <- "A red giant star can curve the space to form a black hole. In absence of stars the space is flat."
Doc6 <- "With exception of the stars the space is filled with blackness making the black holes even harder to see."
Doc7 <- "Our sun is a small star and it will not end as a black hole. It does not have enough mass to curve the space."
Doc8 <- "Very few stars will end as black holes but still the space contains large number of black holes."

doc <- c(Doc1,Doc2,Doc3,Doc4,Doc5,Doc6,Doc7,Doc8) # Merge all strings
corpus <- Corpus(VectorSource(doc))

# Preprocessing
corpus.temp <- tm_map(corpus, removePunctuation) # Remove Punctuation
corpus.temp <- tm_map(corpus.temp, stemDocument, language = "english")# Perform Stemming
dtm <- as.matrix(DocumentTermMatrix(corpus.temp)) # Document term matrix

# Text Classification
library(class) # Using kNN 
train.doc <- dtm[c(1,2,5,6),] # Dataset for which classification is already known
test.doc <- dtm[c(3,4,7,8),] # Dataset you are trying to classify
Tags <- factor(c(rep("cars",2), rep("space",2))) # Tags - Correct answers for the training dataset
prob.test<- knn(train.doc, test.doc, Tags, k = 2, prob=TRUE) # k-number of neighbors considered

# Display Classification Results
a <- 1:length(prob.test)
b <- levels(prob.test)[prob.test]
c <- attributes(prob.test)$prob
result <- data.frame(Doc=a, Predict=b,Prob=c)
result
sum(c)/length(Tags) # Overall probability

sum(prob.test==Tags)/length(Tags) # % Correct Classification











