import csv
import os

# open the cvs
election_csvpath = os.path.join('Resources','election_data.csv')

total_votes = 0
canidates = []



# open the cvs
with open(election_csvpath) as election_csvfile:
    
    #reads each row in the csv as a list
    csvreader = csv.reader(election_csvfile)
    
    #skips the header
    header = next(csvreader)

    #moves to first row of data and grabs the vaules
    row1 = next(csvreader)
    prev_month = int(row1[1]) 
    total_amount = int(row1[1])
    total_months = 1 

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


summary()

# create the ouput file 
output_file = os.path.join("Analysis","output_summary.md")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    output = str(summary())
    datafile.write(output)
    #datafile.write(f"Total: ${total_amount}")
    #datafile.write(f'Average Change: ${change_sum/(total_months-1)}')
    #datafile.write(f'Greatest Increase in Profits: {max_month} (${max_change})')
    #datafile.write(f'Greatest Decrease in Profits: {min_month} (${min_change})')
      

