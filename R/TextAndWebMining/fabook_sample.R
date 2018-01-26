
#####################################
# FACEBOOK
# October 8th, 2017
####################################
library(twitteR)
library(wordcloud)
library(ggplot2)  
library(tm)
library(SnowballC)
setwd("path")
library(Rfacebook)
# App ID

# Use your credentials Old Way
fb.app.id <- "" # Your Credentials 
fb.app.secret <- "" # Your Credentials 
fb.oauth <- fbOAuth(app_id = fb.app.id, app_secret = fb.app.secret, extended_permissions = TRUE)


user <- getUsers("me", token = fb.oauth) 

user$id
user$name
user$first_name
user$last_name
user$gender
user$locale

library(RCurl)
library(RJSONIO)



