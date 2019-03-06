# *** PyBank ***

# Importing the csv module to read the file
import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables that need defining
Month_Counter = 0
Tot_Profits = 0
Ea_Diff = []
Last_Month = 0
Diff_Sum = 0
Max_Inc = 0
Max_Dec = 0
Months_list = []

# Within the csv file...
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Until I need the headers, this just destroys the header row for following script
    csv_header = next(csvreader)

    for row in csvreader:
        # Counting rows for Total Months
        Month_Counter += 1
        # Adding all P/L together
        Tot_Profits += int(row[1])
        # Average of difference from Month i to Month i + 1
        This_Month = row[1]
        # Adding each difference between months to a list
        Ea_Diff.append(int(This_Month) - int(Last_Month))
        Last_Month = row[1]
        # Adding each date to a list to be used in Greatest Increase/Decrease
        Months_list.append(row[0])
    
    # Deleting the first element of the list Ea_Diff, which is just the first P/L value
    Ea_Diff.pop(0)


    for i in Ea_Diff:
        # Summing all of the differences stored in the Ea_Diff list together        
        Diff_Sum += i
        
        # Storing the greatest positive and negative differences from Ea_Diff list
        if i > Max_Inc:
            Max_Inc = i
        elif i < Max_Dec:
            Max_Dec = i

    # Finds and stores the location of the greatest positive and negative differences from Ea_Diff list
    Inc_Index = Ea_Diff.index(Max_Inc) + 1
    Dec_Index = Ea_Diff.index(Max_Dec) + 1

    # Averaging the sum of differences by the number of elements in Ea_Diff list
    Avg_Change = Diff_Sum / len(Ea_Diff)

    Fin_Analysis = f"""    Financial Analysis
    ----------------------------
    Total Months: {Month_Counter}
    Net Total: ${Tot_Profits} 
    Average Change: ${round(Avg_Change, 2)}
    Greatest Increase in Profits: {Months_list[Inc_Index]} (${Max_Inc})
    Greatest Decrease in Profits: {Months_list[Dec_Index]} (${Max_Dec})
    """

print(Fin_Analysis)

output_file = open("PyBank_output.txt", "w")

output_file.write(Fin_Analysis)