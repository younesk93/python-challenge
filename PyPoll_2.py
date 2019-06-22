# Import os module, Pandas and csv file reader

import csv
import os

# Know the current working directory

Current_Path = os.getcwd()
Current_Path 

# '/Users/Younes/Desktop/CLASSWORK/LearnPython/Useful-Repository-master/Resources/PyPoll'

# Assign variables 

Total_Votes = 0 

Poll = {}
Candidates = []
Number_Votes = []
Votes_Percentage = []

output = 'Election_Data.txt'

# Open CSV file

csvpath = os.path.join('Election_Data.csv')
with open(csvpath, newline = '') as csvfile:

# Specify delimiters

        csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 

        csv_header = next(csvfile)

        print('Election Results')
        print('---------------------------------')

# Create loop
            
        for row in csvreader:
            
# Calculate the totals

            Total_Votes += 1
            if row[2] in Poll.keys():
                Poll[row[2]] = Poll[row[2]] + 1
            else:
                Poll[row[2]] = 1

        for key, value in Poll.items():
            Candidates.append(key)
            Number_Votes.append(value)

        for n in Number_Votes:
            Votes_Percentage.append(round(n/Total_Votes*100, 1))

        Data = list(zip(Candidates, Number_Votes, Votes_Percentage))
       
        Winner_List = []
   
        for Name in Data:
            if max(Number_Votes) == Name[1]:
                Winner_List.append(Name[0])

        Winner = Winner_List[0]
        
        if len(Winner_List) > 1:
            for w in range(1, len(Winner_List)):
                Winner = Winner + ", " + Winner_List[w]

# Print Total Votes    

print("Total Votes: " + str(Total_Votes))

print('---------------------------------')

#Print Percentage of the votes

for i in Data:
        print(i[0] + ": " + str(i[2]) +'%  (' + str(i[1]) + ')')

#Print the final winner
print('---------------------------------')

print('Winner: ' + Winner)

print('---------------------------------')

#Output to text file

with open(output, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for i in Data:
        txtfile.writelines(i[0] + ": " + str(i[2]) +'%  (' + str(i[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + Winner + '\n-------------------------')

