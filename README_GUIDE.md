# python-challenge
In this assignment, the two projects were successfully developed. 
Find the below specified information about each project


#PyBank project;
gains array stored change in profit and dates array store the respective dates
counter stored total records in the dataset
As we go through each record;
- we store the dates in the date array 
- calculates the change in profit/loss by subtracting the previous from current value and storing that value in the gains array

The average change is calculated by summing the values in the gains array and diving the sum by the counter(whihc holds total number of record).
Max value in Gains is the greatest increase in profit. We use the index of the greatest profit increase to get the corresponding date.
Min value in Gains gives the worst lost. The index of the worst loss will give the corresponding date.


#PyPoll Project;
Main focus was on the Candidate column
Cand array stores unique candidates and votes list stores the votes for the respective candidate.
if a candidate is not in the cand array, add them and set thier vote count to zero else increase its count by one.
counter will store total number of records
vote will store total number of votes, vote_percent will have the percentage to 3 decimal places
also count the num of votes and store the winner - user with highest vote


