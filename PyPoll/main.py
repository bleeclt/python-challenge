import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')