import csv
import os 

election_csv = "Resources/election_data.csv" 

with open(election_csv, 'r') as csvfile: 
    election_csv = csv.reader(csvfile)
    header = next(election_csv)

    vote_count = 0
    popular_vote = 0 
    candidate_dict = {}

    for row in election_csv:
        vote_count += 1
        candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1

print(f'Election Results')
print(f'=========================')
print(f'Total Votes: {vote_count}')
print(f'=========================')

for candidate, vote in candidate_dict.items(): 
    print(f'{candidate}: {vote / vote_count * 100:.3f}% ({vote})')
    if vote > popular_vote:
        vote = popular_vote
        winner = candidate 

print(f'=========================')
print(f'Winner: {candidate}')
print(f'=========================')        