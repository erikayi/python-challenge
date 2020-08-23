# Using Voter ID, County, & Candidate info to analyze votes

import os
import csv 

election_csv = os.path.join("Resources/election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter =',')
    
    # Find Total # of votes casted. 
    total_votes = [] 
    for row_count, row in enumerate(csvreader, start=0):
        value = int(row['Voter ID'])
        total_votes.append(value)

    # Complet list of candidates received votes.
    list(Candidate) = []
    for row_count, row in enumerate(csvread, start=2):
        value = long(row['Candidate'])
        list(Candidate).append(value) 




print ('-----------------------------------------')
print ('Election Results')
print ('-----------------------------------------')
print ('Total # Of Votes Cast: ', format(row_count))
print ('List Of Candidates: ', list(Candidate)), 'Percentage Of Votes Received: ', 'Total Number Of Votes Received: ')
print ('Winner Of The Election: ')

