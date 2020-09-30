import os
import csv
import collections
from collections import Counter

election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # variable to hold votes list
    votes = []

    # variable to hold candidates list
    candidates = []

    # loop to capture all votes 
    for row in csvreader:
        votes.append(str(row[2]))

print("Election Results")
print("--------------------------")
print(f'Total Votes: {len(votes)}')
print("--------------------------")
    
# dictionary to hold the count of each vote
breakdown = Counter(votes)
percentage = 

# get the key and values of each dictionary item
for key, value in breakdown.items():
        
    print(f'{key}: ({value})')