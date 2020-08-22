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
    sum_profit = 0
    sum_loss = 0
    total_profit_loss = 0
    profit = 0

    for row in csvreader: 
        profit = int(row[1])
        if profit >= 0:
            sum_profit = sum_profit + profit
        elif profit <= 0:
            sum_loss = sum_loss + profit
    total_profit_loss = sum_profit + sum_loss
    print(f'Total Net amount of profit/losses is {total_profit_loss}')

#Find average(mean) of changes in profit/losses in entire data.
    average = total_profit_loss / profit
    print(f'Average of changes in profit/losses is {average}')
    
#Find greatest increase in profits (include both dates & amounts).


#Find greatest decrease in losses (include both dates & amounts).


#Print the analysis to terminal, and export .txt file with results.  