#Module for reading csv files
import os
import csv

#file to be read is in same location as the main file
#open the file
with open('election_data.csv') as election:
    data = csv.reader(election)
    
    #Skip the header
    next(data,None)
    
    #defining variables 
    counter = 0      #count total records
    cand = []        #to store candidates
    votes = {}       #count votes
    v_count = 0      #will count indv candidate vote
    winner = ""      #will hold the winner

    #Loops through the each row and count
    for row in data:
        counter += 1                        #count total records in the dataset
        if row[2] not in cand:              #add to candidate array if not there
           cand.append(row[2])                #creates an array with each candidate
           votes[row[2]] = 0                  #tracks votes for the candidate
        votes[row[2]] = votes[row[2]] + 1     #adds vote count to candidate

#printing results
print(f'\n ELECTION RESULTS \n-------------------------------')
print("Total Votes: ", counter, '\n-----------------------------' )

#display candidate and votes
for candidate in cand:
    vote = votes[candidate]         
    vote_percent =format((vote/counter) * 100, '.3f')   #formats and cal %age
    if vote > v_count:              #find winner by comparing votes
        v_count = vote
        winner = candidate
    print(f"{candidate}: {vote_percent}% ({vote}) ")
print('\n------------------------------')
print('Winner: ', winner ,'\n-------------------------')





