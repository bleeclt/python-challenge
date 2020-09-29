import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    csvheader = next(csvreader)

    # variable to hold date
    date = []
    # variable to hold profit and losses
    pl = []
    # variable to hold the changes in profit/losses between months
    rowchange = []

    
    # create a lists of date and profit/loss columns
    for row in csvreader:
        pl.append(float(row[1]))
        date.append(row[0])

        
# loop through the lists created above
for i in range(1, len(pl)):

    # create new list to hold each profit/loss change between months
    rowchange.append(pl[i] - pl[i - 1])

    # calculate average change
    avgchange = sum(rowchange)/len(rowchange)

    # find max change
    maxchange = max(rowchange)

    # find min change
    minchange = min(rowchange)

    # produce max and min change dates
    maxchange_date = str(date[rowchange.index(max(rowchange))])
    minchange_date = str(date[rowchange.index(min(rowchange))])
    
    
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: $ {sum(pl)}")
print(f"Avereage Change: ${(avgchange)}")
print(f'Greatest Increase in Profits: {maxchange_date} (${maxchange})')
print(f'Greatest Decrease in Profits: {minchange_date} (${minchange})')