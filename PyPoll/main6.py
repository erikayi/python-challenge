# Using Voter ID, County, & Candidate info to analyze votes

import os
import csv 
from collections import Counter

election_csv = os.path.join("Resources/election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    total_votes = [] 
    for row_count, row in enumerate(csvreader, start=0):
        value = int(row['Voter ID'])
        total_votes.append(value)

    votes = ["Khan", "Li", "Correy", "O'Tooley"]
    for row_count, row in enumerate(csvreader, start=2):
        votes_per_candidate = sorted(row['Candidate'])
        votes.append(votes_per_candidate)



        
                





print("---------------------------------------------")
print("Election Results")
print("---------------------------------------------")
print("Total Votes: ", format(row_count))
# print("List Of Candidate: ", format(Candidate), ": {}".format(percentage_won), "Total Votes Received: {}".format(votes_for_candidates))
# print("Winner: ",)

# votes_received_by_winner = max(votes_received)
# index_of_the_winner_name = votes_received.index(votes_received_by_winner)
# winner_name = candidates[index_of_the_winner_name]

# print("{} is the winner with a total of {} votes".format(winner_name, votes_received_by_winner))