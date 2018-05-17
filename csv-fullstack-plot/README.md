
## Installation

To install packages: npm install
To start the application: npm start

# I installed csv-load-sync to read the csv file [1]
to install csv-load-sync : npm install csv-load-sync
#angular chart was aleady installed but in case we need it [3]
to install angular-chart: bower install --save angular-chart.js

# instead to add my services so DataService

# while I like to do a most elegant way I used this simple js loop to parse the object 
for (var i in csv) {
    csv[i].a = parseInt(csv[i].count);
    csv[i].mydate = csv[i].date;
}
# alasql is very primitive and crashed with the name such as total, count, date [3]
# also, I picked alas because I was able to write sql query style instead to group my elements
# instead of do it by myseld

# I didn't find bower angular line chart documentation, then. I got a problem with the format of the data then
# I have to start cooking my data in the results as key/values as the example so, I was able to create and show the chart
# the worst part is the loop to read the results from each query 
i.e
    for (var i in res) {
        res[i].values =  res[i].totalSales;
        res[i].key =  res[i].mydate;
        delete res[i].totalSales;
        delete  res[i].mydate;
      }

# this is pretty much a very unoptimized way to create the two results and return them
# this is because alassql doesn't accept key/values as field names 
# and I wouldn't change the key/values names to create the linechart in the controller 

#added 
  body {
    overflow-y: auto !important;
  }
#to display the 3 graph
#THIS WAS AN IBM EXCERSISE 

# VisualStudio Code Version 1.19.2 (1.19.2)
# nmp -v 5.60
# bower -v 1.8.2


#References 
#[1] https://www.npmjs.com/package/csv-load-sync
#[2] https://www.npmjs.com/package/angular-chart.js/
#[3] https://medium.com/@danacodes/alasql-a-query-language-for-javascript-e1540ac238b4 