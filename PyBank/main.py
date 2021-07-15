import csv
import os

# open the cvs
budget_csvpath = os.path.join('Resources','budget_data.csv')

# open the output file, create a header row, and then write the zipped object to the csv
with open(budget_csvpath) as budget_csvfile:
    csvreader = csv.reader(budget_csvfile, delimiter=",")

    next(csvreader)

    # setting inital variables
    total_months = 0
    total_amount = 0
    monthly_changes = []

    for month in csvreader:   
        total_months += 1
        total_amount += float(month[1])

    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
