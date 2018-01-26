#Forecast_kWh_Demand.R wih my moficications
library("RSNNS")
library("jsonlite")

### Pre-Process Data & Call Neural Network 
Parse.JSON.Input <- function (inputs) 
{
  ix <- grep("Relative_Humidity",inputs$historian$TagName); InputData <-data.frame(inputs$historian$Samples[[ix]]$TimeStamp,stringsAsFactors = FALSE); 
  InputData <-cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outdoor_Dewpoint",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outdoor_Temperature",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("BUE_Stud_Electric_Demand_kW",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Optimal_Electric_Demand_kW",inputs$historian$TagName); InputData <- cbind(InputData, as.numeric(inputs$historian$Samples[[ix]]$Value),stringsAsFactors = FALSE)
  ix <- grep("Outputs.Predicted_Electric_Demand",inputs$parameters$Name); InputData <- cbind(InputData, inputs$parameters$Tag[[ix]],stringsAsFactors = FALSE)
  colnames(InputData) <- c("DATE","Relative_Humidity","Outdoor_Dewpoint","Outdoor_Temperature","Electric_Demand_kW","Optimal_Electric_Demand_kW","TagName")
  return (InputData) # Returned object
}

Forecast.Electric.Demand <- function (Raw_Data) 
{
  library("RSNNS")
  print("2. Inputs sent to function: Forecast.Electric.Demand()")
  # Convert Time Stemps
  Num.Data.Points <- dim(Raw_Data)[1]
  Time.Stamp <- strptime(Raw_Data$DATE,"%Y-%m-%dT%H:%M:%S")
  
  # Select Training Range 
  StartTime <- 1 # which(Time.Stamp=="2014-03-01 01:00:00 EST")
  TrainRange <- StartTime:Num.Data.Points
  print(paste0("Training data start date: ",Time.Stamp[StartTime]))
  
  # Extract Hours field from Time.Stamp
  Hours <- as.numeric(format(Time.Stamp,'%H')) # Replace this Line
  # Insert your code here
  Day.Date <- as.numeric(format(Time.Stamp,'%d'))   
  # Extract Days field from Time.Stamp
  Day.Number <- as.numeric(format(Time.Stamp, '%w'))# Replace this Line
  # Insert your code here
  Day.Number[Day.Number==0]=7
  Day.Name <- weekdays(Time.Stamp)
  # Modify Hours & Days
  temp <- 12-Hours; temp[temp>=0] = 0
  Hours.Modified <- Hours + 2*temp
  Day.Number.Modified <- Day.Number
  
  # Insert your code here
  Day.Number.Modified[Day.Number<6]=1
  Day.Number.Modified[Day.Number==6]=2
  
  print("Extracting Hour_of_Day & Day_of_Week fields from the DATE field Time Stamp ")
  
  # Choose Data to Process 
  Dependent.Ix <- c(2:4) # Select dependent columns
  Dependent.Data <- cbind(Hours.Modified, Day.Number.Modified, Raw_Data[TrainRange,Dependent.Ix]); # X ()
  Independent.Ix <- c(5) # Select Independent columns
  Independent.Data <- Raw_Data[TrainRange,Independent.Ix]; # Y (Actual Electric Demand )
  print("Dependent data tags: ");  print(names(Dependent.Data))
  print("Independent data tags: ");  print(names(Raw_Data[Independent.Ix]))
  
  # Define NuNet Inputs
  inputs <- Dependent.Data # Actual Consumption - used for training
  targets <- Independent.Data # Expected Consumption (Regression data) used as Tags
  Percent.To.Test <- 0.30 # Split the input data into train and test
  print("Define NuNet Inputs: "); print(paste0("Percent of input data to test: ", 100*Percent.To.Test, " %"))
  
  # Train NuNet & Get Predictions
  print("Train NuNet & Get Predictions, please wait... ");
  Predicted.Electric.Demand <- TrainNuNet(inputs,targets,Percent.To.Test) 
  # Predicted.Electric.Demand <- list(rep(0,Num.Data.Points)) # Populate with zero
  print("NuNet Training finished!");
  
  # Actual.Electric.Demand <- Independent.Data 
  # Output <- list(Predicted.Electric.Demand)
  Output <- data.frame("TimeStamp"=Time.Stamp,"Value"=unlist(Predicted.Electric.Demand),"Quality"=3)
  
  return (Output) # Returned object
  
}


TrainNuNet <- function (inputs,targets,Percent.To.Test) 
{
  # Normalize the Data 
  if (is.null(dim(inputs))) # Single Column Input
  {
    z <- max(inputs, na.rm=TRUE) # find Max in Single Input Column
    inputs.scale <- z; targets.scale <- max(targets)
    inputs.normalized <- inputs/inputs.scale # Normalize Data
    targets.normalized <- targets/targets.scale # Normalize Data 
  }
  else # Multi Colum Input
  {
    z <- apply(inputs, MARGIN = 2, function(x) max(x, na.rm=TRUE)) # find Max in Each Input Column
    inputs.scale <- as.vector(z); targets.scale <- max(targets);
    inputs.normalized <- sweep(inputs, 2, inputs.scale, `/`) # Normalize Data
    targets.normalized <- targets/targets.scale # Normalize Data   
  }
  
  
  # Split the Data into Train and Test
  patterns <- splitForTrainingAndTest(inputs.normalized, targets.normalized, ratio = Percent.To.Test) 
  set.seed(13);
  
  # Train NN to folow Actual 
  # The use of an Elman network (Elman 1990) for time series regression.
  model <- elman(patterns$inputsTrain, patterns$targetsTrain,
                 size = c(10, 10), learnFuncParams = c(0.1), maxit = 1300,
                 inputsTest = patterns$inputsTest, targetsTest = patterns$targetsTest,
                 linOut = FALSE)
  # model <- elman(patterns$inputsTrain, patterns$targetsTrain,
  #                size = c(8, 8), learnFuncParams = c(0.1), maxit = 500,
  #                inputsTest = patterns$inputsTest, targetsTest = patterns$targetsTest,
  #                linOut = FALSE)
  
  NN.fitted.Train <- model$fitted.values*targets.scale 
  NN.fitted.Test <- model$fittedTestValues*targets.scale 
  
  Predicted.Electric.Demand <- c(NN.fitted.Train,NN.fitted.Test)
  
  result <- list(Predicted.Electric.Demand)
  
  return (result) # Returned object
}

wrapper <- function(inputJSON.Data){
  # # Import data 
  
  inputs <- fromJSON(inputJSON.Data, flatten=TRUE)
  InputData <- Parse.JSON.Input(inputs) # Turn JSON Input to DataFrame
  print("1. Historian Database input tags imported to R Script:")
  print(names(InputData))
  Output <- Forecast.Electric.Demand(InputData) 
  temp <- as.character( Output$TimeStamp); Output$TimeStamp <- paste0(sub(" ","T",temp),"Z")
  
  # In Historian Format 
  z <- list("TagName"=InputData$TagName[1],ErrorCode=0,"DataType"="DoubleFloat" ,"Samples"=Output)
  
  Predicted.Electric.Demand <- toJSON(list(z),pretty=TRUE)
  print("3. Predicted Electric Demand from NuNet saved to Historian Database")
  
  return(Predicted.Electric.Demand)
}
