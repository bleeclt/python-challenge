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
# breakdown = Counter(votes)
# get the key and values of each dictionary item
#for key, value in breakdown.items():
        
    #print(f'{key}:  ({value})')

# variables to hold the number of votes for each candidate
Khan_count = votes.count("Khan")
Correy_count = votes.count("Correy")
Li_count = votes.count("Li")
OTooley_count = votes.count("O'Tooley")

# determine highest vote count
most_votes = max(Khan_count, Correy_count, Li_count, OTooley_count)
# string to hold winner
Winner = ""

# determine winner 
if most_votes == Khan_count:
    Winner = "Khan"
elif most_votes == Correy_count:
    Winner = "Correy"
elif most_votes == Li_count:
    Winner = "Li"
else:
    Winner = "O'Tooley"

# variables to calculate the percentage of total votes
Khan_per = "{:.3%}".format(Khan_count / len(votes))
Correy_per = "{:.3%}".format(Correy_count / len(votes))
Li_per = "{:.3%}".format(Li_count / len(votes))
OTooley_per = "{:.3%}".format(OTooley_count / len(votes))


print(f'Khan: {Khan_per} ({Khan_count})')
print(f'Correy: {Correy_per} ({Correy_count})')
print(f'Li: {Li_per} ({Li_count})')
print(f"O'Tooley: {OTooley_per} ({OTooley_count})")
print("--------------------------")
print(f'Winner: {Winner}')
print("--------------------------")