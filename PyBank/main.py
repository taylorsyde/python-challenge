import csv
import os

# open the cvs
budget_csvpath = os.path.join('Resources','budget_data.csv')
  
#define variables
change_sum = 0
max_month = ""
max_change = 0
min_month = ""
min_change = 0 

# this list will hold my summary
summary = []

# open the data file and start analysis
with open(budget_csvpath) as budget_csvfile:
    
    #reads each row in the csv as a list
    csvreader = csv.reader(budget_csvfile)
    
    #skip the header
    header = next(csvreader)

    #grabs starting values from first row of data
    row1 = next(csvreader)
    prev_month = int(row1[1]) 
    total_amount = int(row1[1])
    total_months = 1 

    # read the remaining rows and store max, min, and total
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
        prev_month = curr_month


#calculate average change and format
average_change = change_sum/(total_months-1)
average_change = round(average_change,2)

#summary strings
summary.append('Financial Analysis')
summary.append('----------------------------')
summary.append(f"Total Months: {total_months}")
summary.append(f"Total: ${total_amount}")
summary.append(f'Average Change: ${average_change}')
summary.append(f'Greatest Increase in Profits: {max_month} (${max_change})')
summary.append(f'Greatest Decrease in Profits: {min_month} (${min_change})')


#print summary to terminal
for item in summary:
    print(item)

# create the ouput file path
output_path = os.path.join("Analysis","output_summary.md")

# open the output file and then write the a text file
with open(output_path, "w") as output_file:
    for item in summary:
        output_file.write(item + "\n") #you might have to change this part
    