# Import file
import os
import csv

# Input and output data
path = os.path.join("Resources", "election_data.csv")
analysis = os.path.join("Analysis", "pypoll_analysis.txt")

#Variables
candidates = []
votes = []
winning_candidate = ""
winning_percentage = ""
winning_count = 0
total_votes = 0

counter = {
    "Correy" : 0,
    "Khan" : 0,
    "Li" : 0,
    "OTooley" : 0}

#Read CSV
with open(path, "r") as data:
    csv_reader = csv.reader(data)
    next(csv_reader)

    for row in csv_reader:
        candidates.append(row[2])
        votes.append(row)

for candidate in candidates:
    if candidate == "Correy":
        counter["Correy"] += 1
    elif candidate == "Khan":
        counter["Khan"] += 1
    elif candidate == "Li":
        counter["Li"] += 1
    elif candidate == "OTooley":
        counter["OTooley"] += 1

    votes = counter.get(candidate)

    
    correy_vote = int(counter["Correy"])
    khan_vote = int(counter["Khan"])
    li_vote = int(counter["Li"])
    otooley_vote = int(counter["OTooley"])

    total_votes = khan_vote + correy_vote + li_vote + otooley_vote
    correy_percent = (correy_vote / total_votes) * 100
    khan_percent = (khan_vote / total_votes) * 100
    li_percent = (li_vote / total_votes) * 100
    otooley_percent = (otooley_vote / total_votes) * 100
    
    

    if(votes > winning_count):
        winning_count = votes
        winning_candidate = candidate




Output = (
    f"\nElection Results\n-----------------------------------\n"
    f"Total Votes: {len(votes)}\n-----------------------------------\n"
    f"Correy: {round(correy_percent)}% ({counter['Correy']})\n"
    f"Khan: {round(khan_percent)}% ({counter['Khan']})\n"
    f"Li: {round(li_percent)}% ({counter['Li']})\n"
    f"O'Tooley: {round(otooley_percent)}% ({counter['OTooley']})"
    f"-----------------------------------\n"
    f"Winner: {candidate}"
)

print(Output)

with open(analysis, "w") as output_file:
    output_file.write(Output)