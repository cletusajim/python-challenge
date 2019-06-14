#Module for reading csv files
import os
import csv

#file to be read is in same location as the main file
#open the file
with open('budget_data.csv') as budget:
    data = csv.reader(budget)
    
    #Skip the header
    next(data,None)
    
    #defining variables 
    counter = 0    
    avg = 0.0   
    wst_loss = 0
    dates = []
    gains = []
    nw_value = 0   
    prft_chg = 0    
    profit = 0


    #Loops through the each row and count
    for row in data:
        counter += 1                        #count total records in the dataset
#        print(row[1])      #print each row as we loop through
        dates.append(row[0])                #add the dates to the date array
        prft_chg = int(row[1]) - nw_value   #get the profit change between each month
        gains.append(prft_chg)              #store that change in this array
#        print("Change%", gains)  #test/see items in the gains array
        nw_value = int(row[1])              #assign the next value in profit to this variable
        profit += int(row[1])

    avg = (sum(gains))/counter               #get the average change for the profit/loss
    max_chg = max(gains)                     #get maximum gain from the gains array
    max_chg_dt = dates[gains.index(max_chg)] #get the date of the max gain
    max_loss = min(gains)                    #get the max loss or min gain
    max_loss_dt = dates[gains.index(max_loss)]  #get the date of the min gain

print(f'\n Financial Analysis \n-------------------------------')
print("Total Months: ", counter )
print("Total: $", profit )
print("Average Change: ", avg )
print("Greatest Increase in Profits: ", max_chg_dt, " ($",max_chg, ")")
print("Greatest Decrease in Profits: ", max_loss_dt, "($",max_loss, ")")


