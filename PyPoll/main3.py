# Using Voter ID, County, & Candidate info to analyze votes

import os
import csv 
#from statistics 
#import mean

election_csv = os.path.join("Resources/election_data.csv")

votes = {}

for i in range(5):
    candidate = input("Enter the name of the candidate:")
    number_votes = int(input('Enter the number of votes:'))
    votes[candidate] = number_votes

total_votes = sum(votes.values())
max_votes = max(votes.values())

for key, value in votes.items():
    if value == max_votes:
        winner_name = key
        break

    print("{} is the winner with a total of {} votes".format(winner_name, max_votes))

