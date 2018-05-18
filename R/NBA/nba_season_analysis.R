##########################################      s
# 10/16/2017
##########################################
library(googleVis)
library(RCurl)
library(RJSONIO)
library(SportsAnalytics)
library(XML)
library(stringr)
setwd("path")
getwd()

#a)	Retrieve the NBA data for the 2007-2008 season.
nba.season <- "07-08"
nba.data <- fetch_NBAPlayerStatistics(nba.season)
save(nba.data, file="nba.data.RData")
load(file="nba.data.RData")
names(nba.data)
#b)	Subset the data for your favorite team. Show the code you used to find: 
#Get favorite Team #Get Champion Team 
newyork.knicks <- subset(nba.data, Team == 'NYK')
boston.celtics <- subset(nba.data, Team == 'BOS')
boston.celtics.table.chart <- gvisTable(boston.celtics[,c(2,4:12)])
newyork.knicks.table.chart <- gvisTable(newyork.knicks[,c(2,4:12)])

plot(newyork.knicks.table.chart)
plot(boston.celtics.table.chart)

# Which player has the best three point percentage? 
#"ThreesMade"  "ThreesAttempted" 
knicks.goals.Three <- aggregate(newyork.knicks$ThreesMade, by = list(newyork.knicks$Name),FUN = "sum")
names(knicks.goals.Three)<-c("Names","ThreesMade")
knicks.attempts.Three <- aggregate(newyork.knicks$ThreesAttempted, by = list(newyork.knicks$Name),FUN = "sum")
names(knicks.attempts.Three)<-c("Names","ThreesAttempted")
knicks.results.Three <- merge(knicks.goals.Three, knicks.attempts.Three, by = "Names")
fg<-(knicks.goals.Three$ThreesMade/knicks.attempts.Three$ThreesAttempted)*100
knicks.results.Three$ThreePercentage <- fg
knicks.results.Three.sorted <-knicks.results.Three[with(knicks.results.Three, order(-ThreePercentage)),]
head(knicks.results.Three.sorted,3) #top 3


celtics.goals.Three <- aggregate(boston.celtics$ThreesMade, by = list(boston.celtics$Name),FUN = "sum")
names(celtics.goals.Three)<-c("Names","ThreesMade")
celtics.attempts.Three <- aggregate(boston.celtics$ThreesAttempted, by = list(boston.celtics$Name),FUN = "sum")
names(celtics.attempts.Three)<-c("Names","ThreesAttempted")
celtics.results.Three <- merge(celtics.goals.Three, celtics.attempts.Three, by = "Names")
fg<-(celtics.goals.Three$ThreesMade/celtics.attempts.Three$ThreesAttempted)*100
celtics.results.Three$ThreePercentage <- fg
celtics.results.Three.sorted <-celtics.results.Three[with(celtics.results.Three, order(-ThreePercentage)),]
head(celtics.results.Three.sorted,3) #top 3

# o	Which player has played the largest number of minutes?
#"TotalMinutesPlayed"

knicks.minutes <- aggregate(newyork.knicks$TotalMinutesPlayed,by = list(newyork.knicks$Name),FUN = "sum")
names(knicks.minutes)<-c("Names","TotalMinutesPlayed")
head(knicks.minutes[order(-knicks.minutes$TotalMinutesPlayed),],3) #top 3
celtics.minutes <- aggregate(boston.celtics$TotalMinutesPlayed,by = list(boston.celtics$Name),FUN = "sum")
names(celtics.minutes)<-c("Names","TotalMinutesPlayed")
head(celtics.minutes[order(-celtics.minutes$TotalMinutesPlayed),],3) #top 3

# o	Which player has the most "Steals"?
#"Steals"  
knicks.steals <- aggregate(newyork.knicks$Steals,by = list(newyork.knicks$Name),FUN = "sum")
names(knicks.steals)<-c("Names","Steals")
head(knicks.steals[order(-knicks.steals$Steals),],3) #top 3

celtics.steals <- aggregate(boston.celtics$Steals,by = list(boston.celtics$Name),FUN = "sum")
names(celtics.steals)<-c("Names","Steals")
head(celtics.steals[order(-celtics.steals$Steals),],3) #top 3

#c)	Show 5 teams for the 2007-2008 season that have the most wins in descending order. 

#http://www.landofbasketball.com/yearbyyear/2007_2008_standings.htm
webpage <- paste0("http://www.landofbasketball.com/","yearbyyear/2007_2008_standings.htm")
#nwc == nba.western.conference
#nec == nba.eastern.conference
# Team  W L Pct GB
nwc <- readHTMLTable(webpage, which = 1, stringsAsFactors = FALSE)
nec <- readHTMLTable(webpage, which = 2, stringsAsFactors = FALSE)
nba <- rbind(nwc, nec) # combine two conference 
nba[, 3] <- as.numeric(as.character(nba[, 3] )) # converting to numeric 
nba[, 4] <- as.numeric(as.character(nba[, 4] ))
nba[, 5] <- as.numeric(as.character(nba[, 5] ))
nba[, 6] <- as.numeric(as.character(nba[, 6] ))
nba.wins<- aggregate(nba$W,by = list(nba$Team),FUN = "sum")
names(nba.wins)<-c("Team","Wins")
head(nba.wins[order(-nba.wins$Wins),],5) #top 5

#d)	Use at least 5 Google charts (your choice) to show relevant data from this dataset.

nba.table.chart <- gvisTable(nba[,c("Team", "W", "L", "Pct", "GB")])
plot(nba.table.chart)

nba.loses<- aggregate(nba$L,by = list(nba$Team),FUN = "sum")
names(nba.loses)<-c("Team","Loses")
nba.wl <- merge(nba.wins,nba.loses,by = "Team",sort = FALSE)
nba.chart.column <-  gvisColumnChart(head(nba.wl[order(-nba.wl$Wins),],16), 
                                     options=list(width=1300, height=800))
plot(nba.chart.column)

nba.pct<- aggregate(nba$Pct,by = list(nba$Team),FUN = "sum")
names(nba.pct)<-c("Team","Pct")
nba.chart.pie <-  gvisPieChart(head(nba.pct[order(-nba.pct$Pct),],16), 
                               options=list(width=1300, height=800))
plot(nba.chart.pie)

knicks.minutes.gauge <- gvisGauge(head(knicks.minutes[order(-knicks.minutes$TotalMinutesPlayed),],6),
                           options=list(min=0, max=3500,greenFrom=0, greenTo=1000,
                                        yellowFrom=1000, yellowTo=2000,redFrom=2000, redTo=3500,width=1000, height=1000))
plot(knicks.minutes.gauge)

celtics.minutes.gauge <- gvisGauge(head(celtics.minutes[order(-celtics.minutes$TotalMinutesPlayed),],6),
                                  options=list(min=0, max=3000,greenFrom=0, greenTo=1000,
                                               yellowFrom=1000, yellowTo=2000,redFrom=2000, redTo=3000,width=1000, height=1000))
plot(celtics.minutes.gauge)



# Organizational chart
conference <- c()
name <- c("Western","Eastern")
conference[1] <- NA
conference[2] <- "NBA"
conference[3] <- "NBA"
conference[4:18]<- unique(name)[1]
conference[19:33]<- unique(name)[2]
conference
newnode<- c(c("NBA"),name,nba$Team)
newnode
data = data.frame(
  Node =  newnode,
  Parent = conference,
  val = 1:33
)

conference.org.chart <- gvisOrgChart(
  data,idvar="Node", parentvar="Parent",tipvar="val", 
  options=list(width=1000, height=800, allowCollapse=TRUE))
plot(conference.org.chart)

#e)	(20 points) Use gvisGeoChart function to display the location on the world map of the last 5 Basketball World Cup Champions that you can find at: 
webpage <- paste0("http://www.landofbasketball.com/","world_cup_stats/medals_by_year.htm")
#http://www.landofbasketball.com/world_cup_stats/medals_by_year.htm
#wc == world.champions
wc <- readHTMLTable(webpage, which = 1, stringsAsFactors = FALSE)
names(wc)<-c("WorldCup","Space", "Gold", "Silver", "Bronze")
wc <- subset(wc, select = c("WorldCup", "Gold", "Silver", "Bronze")) #remove space column 
wc <- na.omit(wc) # remove NA rows
wc <- wc[2:nrow(wc), ] #remove first element of the table (table headers)
wc.winners <- subset(wc, select = c("WorldCup","Gold")) 
wc.winners$Gold[wc.winners$Gold=="FR of Yugoslavia"] <- "Serbia"
head(wc.winners, 5)
wc.winners.geochart <- gvisGeoChart(head(wc.winners,5),"Gold","WorldCup")
plot(wc.winners.geochart)
wc.winners
