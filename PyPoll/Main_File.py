#Module
import os
import csv

#Variables
Total = 0
Votes = 0
Khan = 0
Li = 0
Correy = 0
OTooley = 0
Candidate = {}

# Open CSV
with open(election_data.csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile)

    # Loop thru looking for Winner
    for row in csvreader:
        votes = votes + 1

        # Candidate is located in Row [2]
        if candidate in row [2]
            candidate = {} + 1
            pass
        else:
            candidate not in row [2]
            index = candidates.index(row[2])

for key, value in candidate.items():
    print(f'{key}: + {value}')

    #Locating Winner
    winner = max (num_votes)
    

# Winner
print("Election Results")
print("-----------------")
print(f"Total Votes: {str(Total)}")
print("-----------------")
print(f"Winner: {winning Candidate}")


