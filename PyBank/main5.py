import os
import csv

budget_csv = os.path.join("Resources/budget_data.csv")


with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)

        dates = []
        for row_count, row in enumerate(csvreader, start=0):
            date_profit = str(row['Date'])
            dates.append(date_profit)

            minimum = [] 
            for row_count, row in enumerate(csvreader, start=1):
                minimum_profit = int(row['Profit/Losses'])
                minimum.append(minimum_profit)

                maximum = []
                maximum_profit = int(row['Profit/Losses'])
                maximum.append(maximum_profit)


maxChangeMonth = dates[dates.index(max(dates))]
maxprofit = maximum[maximum.index(max(maximum))]

minChangeMonth = dates[dates.index(min(dates))]
minprofit = minimum[minimum.index(min(minimum))]

Average_Change = round((sum(totals)/row_count),2)

print ("-------------------------------")
print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}". format(row_count))
print ("Total: $ {}". format(sum(totals)))
print ("Average Change: $", Average_Change)
print ("Greatest Increase in Profits: ", maxChangeMonth, ": $", maxprofit)
print ("Greatest Decrease in Profits: ", minChangeMonth, ": $", minprofit)



output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-------------------------------\n")
    text_file.write ("Total Months: {}\n".format(row_count))
    text_file.write ("Total: $ {}\n".format(sum(totals)))
    text_file.write ("Average Change: $\n", Average_Change)
    text_file.write ("Greatest Increase in Profits: \n", maxChangeMonth, ": $", maxprofit)
    text_file.write ("Greatest Decrease in Profits: \n", minChangeMonth, ": $", minprofit)
    