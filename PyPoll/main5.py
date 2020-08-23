# Using Voter ID, County, & Candidate info to analyze votes

import os
import csv 

election_csv = os.path.join("Resources/election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    total_votes = [] 
    for row_count, row in enumerate(csvreader, start=0):
        value = int(row['Voter ID'])
        total_votes.append(value)

        Candidate = [max(10)] 
        Votes = []
        for row_count, row in enumerate(csvreader, start=2):
            Candidate_name = str(row['Candidate'])
            count_votes = int(row['Voter ID'])
            # Candidate = [Khan, Correy, Li]
            Candidate.apprend(Candidate_name)
            Votes.append(count_votes)

                





print("---------------------------------------------")
print("Election Results")
print("---------------------------------------------")
print("Total Votes: ", format(row_count))
print("List Of Candidate: ", format(Candidate))

# votes_received_by_winner = max(votes_received)
# index_of_the_winner_name = votes_received.index(votes_received_by_winner)
# winner_name = candidates[index_of_the_winner_name]

# print("{} is the winner with a total of {} votes".format(winner_name, votes_received_by_winner))