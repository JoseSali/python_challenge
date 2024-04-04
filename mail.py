import os
import csv

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the file path using os.path.join()
budget_path = os.path.join(script_dir, "PyBank", "Resources")
budget_csv = 'budget_data.csv'
file_path_buget = os.path.join(budget_path, budget_csv)

# Lists to store data
Date = []
Profit_Loss = []

# Open the CSV file in read mode
with open(file_path_buget, 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile, delimiter= ",")
    
    # Store the header row
    header = next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append data from each row to respective lists
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))  # Convert Profit/Loss to integers

# Total number of months
total_months = len(Date)

# Calculate the changes in Profit/Losses over the entire period
changes = [Profit_Loss[i + 1] - Profit_Loss[i] for i in range(len(Profit_Loss) - 1)]

# Average of the changes in Profit/Losses
average_change = sum(changes) / len(changes)

# Greatest increase in profits (date and amount)
max_increase = max(changes)
max_increase_date = Date[changes.index(max_increase) + 1]  # Add 1 to get the date corresponding to the change

# Greatest decrease in profits (date and amount)
max_decrease = min(changes)
max_decrease_date = Date[changes.index(max_decrease) + 1]  # Add 1 to get the date corresponding to the change

# Net total amount of Profit/Losses
net_total = sum(Profit_Loss)

# Print the results
print(f"Header: {header}")
print("----------------------------------")
print("Financial Analysis")
print("----------------------------------")
print(f"Header: {header}")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------

election_Path = budget_path = os.path.join(script_dir, "PyPoll", "Resources")
elecrion_Csv = "election_data.csv"
file_path_Election = os.path.join(election_Path, elecrion_Csv)

def election_results(csv_file):
    # Read data from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        votes = [row[2] for row in reader]  # Assuming candidate IDs are in the third column
    
    total_votes = len(votes)
    
    # Counting votes for each candidate
    candidate_votes = {}
    for candidate in votes:
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1
    
    # Calculating percentage of votes for each candidate
    candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
    
    # Finding the winner
    winner = max(candidate_votes, key=candidate_votes.get)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        percentage = candidate_percentages[candidate]  # Using pre-calculated percentages
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

election_results(file_path_Election)
