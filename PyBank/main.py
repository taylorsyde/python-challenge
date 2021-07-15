import csv
import os

def summary():
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_amount}")
    print(f'Average Change: ${change_sum/total_months}')
    print(f'Greatest Increase in Profits: {max_month} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_month} (${min_change})')

# open the cvs
budget_csvpath = os.path.join('Resources','budget_data.csv')

prev_month = 0    
total_months = 0
total_amount = 0
change_sum = 0
max_month = ""
max_change = 0
min_month = ""
min_change = 0 

# open the output file, create a header row, and then write the zipped object to the csv
with open(budget_csvpath) as budget_csvfile:
    
    #reads each row in the csv as a list
    csvreader = csv.reader(budget_csvfile)
    
    #skips the header
    next(csvreader)

    for month in csvreader:
        curr_month = int(month[1])
        total_months += 1
        total_amount += curr_month
        curr_change = curr_month - prev_month 
        change_sum += curr_change
        if curr_change >= max_change:
            max_change = curr_change
            max_month = month[0]
        if curr_change <= min_change:
            min_change = curr_change
            min_month = month[0]
        month[1] = prev_month
        
summary()