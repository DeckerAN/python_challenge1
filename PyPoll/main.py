# *** PyPoll ***

# Importing the csv module to read the file
import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables that need defining
Vote_Counter = 0
Candidates = {}
Max_Votes = 0
Draw_Counter = 0

# Within the csv file...
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Until I need the headers, this just destroys the header row for following script
    csv_header = next(csvreader)

    for row in csvreader:
        # Counting rows for Total Votes
        Vote_Counter += 1
        # Adding each unique candidate to create a complete dict of candidates as keys...
        if row[2] not in Candidates:
            Candidates[row[2]] = 0
        # ... and their votes as values
        else:
            Candidates[row[2]] += 1
    
    # This finds the winner by which key has the highest value (which candidate has the most votes)
    for kCand in Candidates:
        if Max_Votes < Candidates[kCand]:
            Max_Votes = Candidates[kCand]
            Winner = kCand
    
    # If there is a draw, this will show that there is one and not declare a winner.
    for _, votes in Candidates.items():
        if votes == Max_Votes:
            Draw_Counter += 1


    if Draw_Counter > 1:
        Result = "It's a DRAW"
    else:    
        Result = Winner

print(f"""
Election Results
----------------------------
Total Votes: {Vote_Counter}
----------------------------""")
# Printing each key (candidate), each value (votes) over total votes to get percentage of votes, and each value (votes)
for k, v in Candidates.items():
        print(k + ": " + str(round((v / Vote_Counter)* 100, 3)) + "% (" + str(v) + ")")    
print(f"""----------------------------
Winner: {Result}
    """)

# Writes the Election Results to the text file, PyPoll_output.txt
output_file = open("PyPoll_output.txt", "w")

output_file.write(f"""Election Results
----------------------------
Total Votes: {Vote_Counter}
----------------------------
""")
for k, v in Candidates.items():
        output_file.write(k + ": " + str(round((v / Vote_Counter)* 100, 3)) + "% (" + str(v) + ")      ")    
output_file.write(f"""
----------------------------
Winner: {Result}
    """)