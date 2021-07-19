#import dependancies
import csv
import os

# create the path to data
election_csvpath = os.path.join('Resources','election_data.csv')

# define variables
total_votes = 0
candidates = ['Khan',"Li","Correy","O'Tooley"]
votes_by_candidate = [0,0,0,0]
percent_by_candidate = []

dashbreak = ('----------------------------')


#create function for calculating, formatting and printing %
def percent(x):
    num = x/total_votes
    percentage = "{:.2%}".format(num)
    return(percentage)

# open the cvs and begin reading
with open(election_csvpath) as election_csvfile:
    
    #reads each row in the csv as a list
    csvreader = csv.reader(election_csvfile)
    
    #skip the header
    header = next(csvreader)

    #read each row and tally votes
    for row in csvreader:
        vote_cast = row[2]
        total_votes += 1
        if vote_cast == candidates[0]:
            votes_by_candidate[0] += 1
        elif vote_cast == candidates[1]:
            votes_by_candidate[1] += 1
        elif vote_cast == candidates[2]:
            votes_by_candidate[2] += 1
        elif vote_cast == candidates[3]:
            votes_by_candidate[3] += 1

#populate precent of vote by canidate list
for _ in range(0,4):
    percent_by_candidate.append(percent(votes_by_candidate[_]))


# use list comprehension to convert my lists to dictionary
# the internet told me this works, but I only understand half of what is happening
results_dict = dict()
results_dict = {candidates[i]: votes_by_candidate[i] for i in range(len(candidates))}
#this sorts the dict from most highest to lowest votes
#since sort returns a list, it has to be turned back into a dict *lord have mercy*
sorted = sorted(results_dict.items(), key = lambda kv: kv[1], reverse=True)
sorted_results_dict = dict(sorted)


#find the winner and reports the name and string
#this creates a list of the keys(names) and grabs the first one
winner = list(sorted_results_dict.keys())[0]

#this stores the results print outs
summary = []

# strings to be printed in final results
summary.append('Election Results')
summary.append(dashbreak)
summary.append(f'Total Votes: {total_votes}')
summary.append(dashbreak)

#loops thru the dictonary, prints line and adds to results output list
for name, votes in sorted_results_dict.items():
    per = percent(votes)
    summary.append(f'{name}: {per} ({votes})')

summary.append(dashbreak)
summary.append(f'Winner: {winner}')
summary.append(dashbreak)


#print the results to the terminal
for item in summary:
    print(item)

# create the ouput file 
output_file = os.path.join("Analysis","election_results.md")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    for item in summary:
        datafile.write(item + '\n')

