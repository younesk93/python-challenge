# Import os module and csv file reader

import os
import csv

# Know the current working directory

Current_Path = os.getcwd()
Current_Path

#'/Users/Younes/Desktop/CLASSWORK/LearnPython/Useful-Repository-master/Resources/PyBank'

# Assign variables 

total_months = 0
total_revenue = 0
this_month_revenue = 0

prev_revenue = 0
revenue_change = 0
revenue_changes = []

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

output = "budget_analysis.txt"


# Open csv file

csvpath = os.path.join('Budget_Data.csv')
with open(csvpath, newline = '') as csvfile:

# Specify delimiters

        csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 

        csv_header = next(csvfile)
    
        print('Financial Analysis')
        print('---------------------------------')

# Create loop

        for row in csvreader:
            
# Calculate the totals
            
            this_month_revenue = int(row[1])
            total_months = total_months + 1
            total_revenue = total_revenue + this_month_revenue 
            
            revenue_change = int(row[1]) - prev_revenue
            prev_revenue = int(row[1])

            if (revenue_change > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = revenue_change

            if (revenue_change < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = revenue_change
            
            revenue_changes.append(int(row[1]))           
            
        revenue_avg = sum(revenue_changes) / len(revenue_changes)
           
# Print Total Months            
print("Total Months: " + str(total_months))

# Print Total Revenue
print("Total Revenue: " + "$" + str(total_revenue))

# Print Average Change
print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))

# Print Greatest increase:
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 

# Print Greatest decrease:
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

# Print to text Files

with open(output, "w") as txt_file:
    
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write('---------------------------------')
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
