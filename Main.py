Budegt_Data
#Budget_Data
import pandas as pd

#Load the financial dataset
df = pd.read_csv ("34,2: /budget_data (1).csv")

#Print the first 5 rows of the dataset
print(df.head())

# Calculate the total number of months
total_months = len(df)

# Calculate the net total amount of "Profit/Losses"
net_total = df['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses"
df['Change'] = df['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = df['Change'].mean()

# Print the results
print(f'Total Months: {total_months}')
print(f'Net Total: {net_total}')
print(f'Average Change: {average_change}')


#Election_Data

import csv 
import collections

# Load the election data from the CSV file
with open('') as csvfile:64,2: /election_data.csv
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    data = [row for row in reader]

# Calculate the total number of votes cast
total_votes = len(data)

# Create a dictionary to store the votes for each candidate
candidate_votes = collections.defaultdict(int)
for row in data:
    candidate_votes[row[2]] += 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Calculate the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("Candidates:")
for candidate in candidate_votes:
    print(f"  {candidate}: {candidate_votes[candidate]} votes ({candidate_percentages[candidate]:.2f}%)")
print(f"Winner: {winner}")
