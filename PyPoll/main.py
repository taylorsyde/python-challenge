import csv
import os

# open the cvs
election_csvpath = os.path.join('Resources','election_data.csv')

# open the output file, create a header row, and then write the zipped object to the csv
with open(election_csvpath) as election_csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election_csvreader = csv.reader(election_csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(election_csvreader)
    print(f"CSV Header: {csv_header}")
