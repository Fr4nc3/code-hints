# RSNNS energy Consumption Forecast
rm(list=ls()); cat("\014") # clear all
library("RSNNS")
source("Forecast_kWh_Demand.R")
# source("Forecast_kWh_Demand_Student.R") 

# Read Data from CSV
Path.2.Files <- file.path("Data","OficeBuildingData.csv") # Path to CSV File
InputData <- read.csv(Path.2.Files,stringsAsFactors = FALSE,
                      blank.lines.skip = TRUE,header=T) # Read CSV File


# Call Forecast Function to Train NN & Obtain Predictions
Output <- Forecast.Electric.Demand(InputData)
  

# Plot Results 
Range.to.Plot <- seq(from = round(dim(InputData)[1]*(1-Output$Percent.To.Test)), to = dim(InputData)[1])
Title <- "NN Trained to Model Office building Energy Consumption based on Temperature, Humidity and Dewpoint"
Title <- paste(Title,paste0("(Train End Date is ", Output$TimeStamp[Range.to.Plot[1]]),")")

# ### ====== Claculate Residuals ====
Y <- InputData$Electric.Demand..kW.; Yp <- unlist(Output$Predicted.Electric.Demand)
R2 <- 1 - sum( (Yp-Y )^2 ) / sum( (Y-mean(Y) )^2 ) # Coeff of determination (R-squared)
Title <- paste0(Title,"; R Squared:",round(R2,2))


# ### ====== Plot Results ====
library(plotly)
PlotData <- data.frame(x=Output$TimeStamp, 
                       y1=InputData$Electric.Demand..kW., 
                       y2=unlist(Output$Predicted.Electric.Demand))

p <- plot_ly(PlotData, x=~x, y=~y1, name = 'Actual Electric Demand (kW)', type = 'scatter', mode = 'lines')
p <- add_trace(p,y=~y2, name = 'RNN Forecasted Demand (kWh)', mode = 'lines', symbol = I(1), marker = list(size = 5)) # add another line


p <- p %>% layout(title = Title,
                  xaxis = list(title = 'Date',
                               zeroline = TRUE),
                  yaxis = list(title = 'Electric Demand (kW)',
                               range = c(0,max(InputData$Electric.Demand..kW.))))

p # To Plot type "p" in console





  



