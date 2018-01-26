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
