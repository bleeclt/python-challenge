import os
import csv


election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # variable to hold votes list
    votes = []

    # variable to hold candidates list
    candidates = []

    # variables to hold vote count per candidate
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0

    # loop to capture all votes 
    for row in csvreader:
        votes.append(str(row[2]))



# loop to build candidates list
for x in votes:
    if x not in candidates:
        candidates.append(x)

# print(len(candidates))
# print(candidates) 
 
# loop to count votes for each candidate   
for i in range(0, len(votes)):

    if votes[i] == candidates[0]:
        Khan_count += 1
# print(Khan_count)

    elif votes[i] == candidates[1]:
        Correy_count += 1

    elif votes[i] == candidates[2]:
        Li_count += 1

    else:
        OTooley_count +=1

## Alternate method I used intially but less clean and required importing counter
    #for i in range(1, len(candidates))
    #   print(candidates)
        
    # dictionary to hold the count of each vote
    # breakdown = Counter(votes)
    # get the key and values of each dictionary item
    #for key, value in breakdown.items():
            
        #print(f'{key}:  ({value})')

    # variables to hold the number of votes for each candidate
    #Khan_count = votes.count("Khan")
    #Correy_count = votes.count("Correy")
    #Li_count = votes.count("Li")
    #OTooley_count = votes.count("O'Tooley")

# determine highest vote count
most_votes = max(Khan_count, Correy_count, Li_count, OTooley_count)

# string to hold winner
Winner = ""

# determine winner 
if most_votes == Khan_count:
    Winner = candidates[0]
elif most_votes == Correy_count:
    Winner = candidates[1]
elif most_votes == Li_count:
    Winner = candidates[2]
else:
    Winner = candidates[3]

# variables to calculate the percentage of total votes
Khan_per = "{:.3%}".format(Khan_count / len(votes))
Correy_per = "{:.3%}".format(Correy_count / len(votes))
Li_per = "{:.3%}".format(Li_count / len(votes))
OTooley_per = "{:.3%}".format(OTooley_count / len(votes))

# print results on screen
print("Election Results")
print("--------------------------")
print(f'Total Votes: {len(votes)}')
print("--------------------------")
print(f'{candidates[0]}: {Khan_per} ({Khan_count})')
print(f'{candidates[1]}: {Correy_per} ({Correy_count})')
print(f'{candidates[2]}: {Li_per} ({Li_count})')
print(f'{candidates[3]}: {OTooley_per} ({OTooley_count})')
print("--------------------------")
print(f'Winner: {Winner}')
print("--------------------------")

# print results to .txt file
with open("Election_Results.txt", "a") as f:
    print("Election Results", file=f)
    print("--------------------------", file=f)
    print(f'Total Votes: {len(votes)}', file=f)
    print("--------------------------")
    print(f'{candidates[0]}: {Khan_per} ({Khan_count})', file=f)
    print(f'{candidates[1]}: {Correy_per} ({Correy_count})', file=f)
    print(f'{candidates[2]}: {Li_per} ({Li_count})', file=f)
    print(f'{candidates[3]}: {OTooley_per} ({OTooley_count})', file=f)
    print("--------------------------", file=f)
    print(f'Winner: {Winner}', file=f)
    print("--------------------------", file=f)