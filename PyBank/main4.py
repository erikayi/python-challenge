import os 
import csv

csvpath = os.path.join("Resources/budget_data.csv")

print("=================================================")
print("Financial Analysis")
print("=================================================")

#Find the total # of months in entire data.
#Read the csv file.
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #Total number of months included in the date. 
    csvfile.seek(0)
    next(csvreader)
    
    row_count = sum(1 for row in csvreader) 

    print(f"Total Months: {row_count}")

#Find Total Net amount of profit/losses in entire data.
   netTotal = 0

   #Define function
   def budgetAudit(budgetData):
       global netTotal
       global netDifference

       #Find Net Total of profit/losses.
       netTotal = netTotal + int(row[1]) 

    #Read in the csv file
    with open(budget_data.csv, 'r') as csvfile:

        #Split the data on commas
        csvreader = csv.reader(csvfile, delimiter = ',')
        header = next(csvreader)
        
        #Loop through the data.
        for row in csvreader: 
            totalCol = list(row)
            totalCol.pop([0])
            print(totalCol)

            #Run the budgetAudit function
            budgetAudit(row)

#Find average(mean) of changes in profit/losses in entire data.
    

#Find greatest increase in profits (include both dates & amounts).


#Find greatest decrease in losses (include both dates & amounts).


#Print the analysis to terminal, and export .txt file with results.  