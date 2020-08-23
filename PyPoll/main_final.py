# Analyze voting poll using data in csv file.

# import csv and os.
import csv
import os 

# define the location of the data.
election_csv = "Resources/election_data.csv" 

# open the data. 
with open(election_csv, 'r') as csvfile: 
    election_csv = csv.reader(csvfile)
    header = next(election_csv)

# define the values. 
    vote_count = 0
    popular_vote = 0 
    candidate_dict = {}

# find total number of votes cast. 
    for row in election_csv:
        vote_count += 1
        candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1

# print the results using print() function. 
print(f"=========================")
print(f'Election Results')
print(f'=========================')
print(f'Total Votes: {vote_count}')
print(f'=========================')

# Discover complete list of candidates received the most votes. 
for candidate, vote in candidate_dict.items(): 

    # Find the percentage of votes that each candidate received.
    # Find the total number of votes each candidate won.  
    won_candidate = (f'{candidate}: {vote / vote_count * 100:.3f}% ({vote})')
    print(won_candidate)

    # Find the winner of the election based on the popular vote. 
    # Use If and greater than function to find who has the most votes to win the election.
    if vote > popular_vote:
        winner = candidate 

# print the results using print() function. 
print(f'=========================')
print(f'Winner: {candidate}')
print(f'=========================')        

# Finalize the script and Export to a .txt. file with results.
output_file = os.path.join("Analysis.txt")

with open(output_file, "w") as text_file:

    text_file.write ("Election Results\n")
    text_file.write ("===========================\n")

    text_file.write ("Total Votes: {}\n".format(vote_count))
    text_file.write ("===========================\n")

    text_file.write ("{}\n".format(won_candidate))
    text_file.write ("===========================\n")

    text_file.write ("Winner: {}\n".format(candidate))
    
    