#import dependancies
import csv
from io import RawIOBase
import os

# create the path to data
election_csvpath = os.path.join('Resources','election_data.csv')

# define variables
total_votes = 0
canidates = ["Khan","Li","Correy","O'Tooley"]
votes_by_canidate = [0,0,0,0]

# open the cvs and begin
with open(election_csvpath) as election_csvfile:
    
    #reads each row in the csv as a list
    csvreader = csv.reader(election_csvfile)
    
    #skips the header
    header = next(csvreader)

    #read each row and analyze
    for row in csvreader:
        vote_cast = row[2]
        total_votes += 1
        if vote_cast == canidates[0]:
            votes_by_canidate[0] += 1
        elif vote_cast == canidates[1]:
            votes_by_canidate[1] += 1
        elif vote_cast == canidates[2]:
            votes_by_canidate[2] += 1
        elif vote_cast == canidates[3]:
            votes_by_canidate[3] += 1



print(total_votes)
print(canidates)
print(votes_by_canidate)

#this stores the results print outs
results = []

# strings to be printed in final results
results.append('Election Results')
results.append('----------------------------')


#print the results to the terminal
for item in results:
    print(item)

# create the ouput file 
output_file = os.path.join("Analysis","election_results.md")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    for item in results:
        datafile.write(item + '\n')

      

