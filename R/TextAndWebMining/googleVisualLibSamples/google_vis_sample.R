##########################################
# 10/15/2017
##########################################
setwd("path")
getwd()
# from Module 6 Lecure 2
library(googleVis)
library(RCurl)
library(RJSONIO)
library(SportsAnalytics)
library(XML)
library(stringr)
# PART 1
webpage <- paste0("http://powerful-meadow-8588.herokuapp.com/","data/12months_departures_joiners.json", sep="")
webpage
data <- fromJSON(getURL(webpage))

save(data, file="glitch1.RData")
load(file="glitch1.RData")

nodes.info <- do.call("rbind",lapply(data$nodes, data.frame))
# a)	Using the aggregate function, compute the data frame for the total players joining each month. Names the columns as Month and Joining.
aggregate.month <- aggregate(nodes.info$joining,by = list(nodes.info$month),FUN = "sum")
names(aggregate.month) <- c("Month","Joining")
aggregate.month

# b)	Using the aggregate function, compute the data frame for the total players departing each month. Names the columns as Month and Departing.
aggregate.departing <- aggregate(nodes.info$departing,by = list(nodes.info$month),FUN = "sum")
names(aggregate.departing) <- c("Month","Departing")
aggregate.departing

# c)	Merge the two data frames by Month column with sort option as FALSE.
merge.data <- merge(aggregate.month,aggregate.departing,by = "Month",sort = FALSE)
merge.data
# d)	Show month-by-month comparison of the above numbers using the Google Line chart and Google Column chart. Merge the two into a single chart.
chart1.line <- gvisLineChart(merge.data,options=list(width=1000, height=800))#
plot(chart1.line)

chart2.column <- gvisColumnChart(merge.data,options=list(width=1000, height=800)) #
plot(chart2.column)

chart3.merge <- gvisMerge(chart1.line,chart2.column)
plot(chart3.merge)

chart4.combo <- gvisComboChart(merge.data, xvar = "Month", yvar = c("Joining","Departing"),
                               options = list(seriesType = "line",series = '{1:{type : "bars"}}')) #width=1400,
plot(chart4.combo)
# e)	Show the Google Gauge chart with default options for the monthly departing data. Use the range from 0 to 4030.
chart5.gauge <- gvisGauge(aggregate.departing, options=list(min=0, max=4030, width=800, height=800)) #
plot(chart5.gauge)
# f)	Show the Google Gauge chart for the monthly departing data with the green range 0 - 1000, yellow range 1000 - 2000, and the red range 2000 - 4030.
chart6.gauge2 <- gvisGauge(aggregate.departing,
                           options=list(min=0, max=4030,greenFrom=0, greenTo=1000,
                          yellowFrom=1000, yellowTo=2000,redFrom=2000, redTo=4030,width=800, height=800))
plot(chart6.gauge2)


#Part 2
# a)	Retrieve the NBA data for the 13-14 season.
nba1314 <- fetch_NBAPlayerStatistics("13-14")
save(nba1314, file="nba1314.RData")
load(file="nba1314.RData")
names(nba1314)

# [1] "League"              "Name"                "Team"                "Position"            "GamesPlayed"         "TotalMinutesPlayed"  "FieldGoalsMade"      "FieldGoalsAttempted" "ThreesMade"         
# [10] "ThreesAttempted"     "FreeThrowsMade"      "FreeThrowsAttempted" "OffensiveRebounds"   "TotalRebounds"       "Assists"             "Steals"              "Turnovers"           "Blocks"             
# [19] "PersonalFouls"       "Disqualifications"   "TotalPoints"         "Technicals"          "Ejections"           "FlagrantFouls"       "GamesStarted"       
# b)	Which player has the best field point percentage?
players.goals <- aggregate(nba1314$FieldGoalsMade,by = list(nba1314$Name),FUN = "sum")
names(players.goals)<-c("Names","FieldGoalsMade")

players.attempts <- aggregate(nba1314$FieldGoalsAttempted,by = list(nba1314$Name),FUN = "sum")
names(players.attempts)<-c("Names","FieldGoalsAttempted")

typeof(players.goals)

results.players.goals <- merge(players.goals,players.attempts,by = "Names")
#results
#FG% = field goals made / field goals attempted

fg<-(players.goals$FieldGoalsMade/players.attempts$FieldGoalsAttempted)*100
#fg
results.players.goals$FieldGoalPercentage <- fg
results.players.goals
results.players.goals.sorted <-results.players.goals[with(results.players.goals, order(-FieldGoalPercentage)),]
head(results.players.goals.sorted,3) #top 3
# c)	Which player has the best free throw percentage?
#"FreeThrowsMade"      "FreeThrowsAttempted"
players.goals.free <- aggregate(nba1314$FreeThrowsMade,by = list(nba1314$Name),FUN = "sum")
names(players.goals.free)<-c("Names","FreeThrowsMade")

players.attempts.free <- aggregate(nba1314$FreeThrowsAttempted,by = list(nba1314$Name),FUN = "sum")
names(players.attempts.free)<-c("Names","FreeThrowsAttempted")

results.free <- merge(players.goals.free, players.attempts.free, by = "Names")
#results
fg<-(players.goals.free$FreeThrowsMade/players.attempts.free$FreeThrowsAttempted)*100
#fg
results.free$FreeThrowsPercentage <- fg
results.free
results.free.sorted <-results.free[with(results.free, order(-FreeThrowsPercentage)),]
head(results.free.sorted,3) #top 3
# d)	Which player has the best three-point percentage?
#"ThreesMade"  "ThreesAttempted" 
players.goals.Three <- aggregate(nba1314$ThreesMade,by = list(nba1314$Name),FUN = "sum")
names(players.goals.Three)<-c("Names","ThreesMade")

players.attempts.Three <- aggregate(nba1314$ThreesAttempted,by = list(nba1314$Name),FUN = "sum")
names(players.attempts.Three)<-c("Names","ThreesAttempted")

results.Three <- merge(players.goals.Three, players.attempts.Three, by = "Names")
#results

fg<-(players.goals.Three$ThreesMade/players.attempts.Three$ThreesAttempted)*100
#fg
results.Three$ThreePercentage <- fg
results.Three
results.Three.sorted <-results.Three[with(results.Three, order(-ThreePercentage)),]
head(results.Three.sorted,3) #top 3


# e)	Show the top 10 players in terms of TotalPoints, arranged from the highest to lowest.
players.totalpoints <- aggregate(nba1314$TotalPoints,by = list(nba1314$Name),FUN = "sum")
names(players.totalpoints)<-c("Names","TotalPoints")
head(players.totalpoints[order(-players.totalpoints$TotalPoints),],10) #top 10

# f)	Use at least 5 Google charts (your choice) to show relevant data from this dataset.
chart.free.line <- gvisLineChart(head(players.goals.free[order(-players.goals.free$FreeThrowsMade),],10),
                                 options=list(width=1000, height=800))
plot(chart.free.line)

chart.goals.column <- gvisColumnChart(head(players.goals[order(-players.goals$FieldGoalsMade),],10),
                                      options=list(width=1000, height=800))
plot(chart.goals.column)

chart.totalpoint.pie <- gvisPieChart(head(players.totalpoints[order(-players.totalpoints$TotalPoints),],10),
                                     options=list(width=1000, height=800) )

plot(chart.totalpoint.pie)

teams.PersonalFouls <- aggregate(nba1314$PersonalFouls,by = list(nba1314$Team),FUN = "sum")
names(teams.PersonalFouls)<-c("Teams","PersonalFouls")


teams.fouls.bar.chart <- gvisBarChart(head(teams.PersonalFouls[order(-teams.PersonalFouls$PersonalFouls),],10),
                         options=list(legend="Fouls"))
plot(teams.fouls.bar.chart)

newyork.knicks <- subset(nba1314, Team == 'NYK')

newyork.knicks.table.chart <- gvisTable(newyork.knicks[,c(2,4:12)])
plot(newyork.knicks.table.chart)


#Part 3
webpage <- paste0("http://www.landofbasketball.com/","championships/year_by_year.htm")
nba <- readHTMLTable(webpage,which = 1, stringsAsFactors = FALSE)
names(nba) <- c("Input")
nba[1, "Input"]
nba$Split <- strsplit(nba$Input, split='(\n|\t)')
nba[1, "Split"]

nba$Year <-  sapply(nba$Split,FUN = function (x)substr(x[[1]], 3, 7))
nba$Winner <- sapply(nba$Split,FUN = function (x) str_trim(x[[5]]))
nba$Series <- sapply(nba$Split, FUN = function (x) str_trim(x[[7]]))
nba$Opponent <- sapply(nba$Split, FUN = function (x)str_trim(x[[8]]))

# nba$Split <- NULL
# nba$Input <- NULL

# a)	How many times was the series swept, i.e., decided by the series score 4-0?
nba[which(nba$Series=="4-0"),]
nrow(nba[which(nba$Series=="4-0"),])
# b)	How many times was the series decided by game 7?  (Series score 4-3)
nba[which(nba$Series=="4-3"),]
nrow(nba[which(nba$Series=="4-3"),])
# c)	Show 5 teams that have the most wins in descending order.
nba$Winner
winner.table <- table(nba$Winner)
winners <- as.data.frame(winner.table)
names(winners)<-c("Winner","Frequency")
head(winners[order(-winners$Frequency),],5)
# d)	Create a subset of the lecture data frame with championship data from the last championship to the 1968 season. 
# Using the split data column from the lecture example, add a new column showing the Finals MVP. Show the players
# who won the FinalsMVP award more than once.
nba$FinalsMVP <- sapply(nba$Split, FUN = function (x) str_trim(sub('\\(.*', '', x[[16]]))) #remove the team name too

nba$FinalsMVP

mvp.table <- table(nba$FinalsMVP)
mvps <- as.data.frame(mvp.table)
names(mvps)<-c("FinalsMVP","Frequency")
mvps  <- mvps[3:nrow(mvps), ] # remove empty space and -
head(mvps[order(-mvps$Frequency),],10)












