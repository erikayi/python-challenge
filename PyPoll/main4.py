# Using Voter ID, County, & Candidate info to analyze votes

import os
import csv 

election_csv = os.path.join("Resources/election_data.csv")

candidates = []
votes_received = []

for i in range(5):
    candidate = raw_input("Enter the name of the candidate:")
    number_votes = int(raw_input('Enter the number of votes:'))
    candidates.append(candidate)
    votes_received.append(number_votes)

total_votes = sum(votes_received)
votes_received_by_winner = max(votes_received)
index_of_the_winner_name = votes_received.index(votes_received_by_winner)
winner_name = candidates[index_of_the_winner_name]

print("{} is the winner with a total of {} votes".format(winner_name, votes_received_by_winner))