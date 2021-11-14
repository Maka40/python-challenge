# import file
import csv
import os

# load and output
path = os.path.join("Users", "makar", "python-challenge", "PyBank", "Resources", "budget_data.csv")
analysis = os.path.join("Users", "makar", "python-challenge","PyBank", "Analysis", "budget_analysis.txt")

# Variables
months = []
changes = []
profit_loss = []

# Read csv
with open(path, 'r') as data_1:
    csv_reader = csv.reader(data_1)
    next(csv_reader)


    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

for i in range(1, len(profit_loss)):
    changes.append((int(profit_loss[i]) - int(profit_loss[i-1])))

Output = (
    f"\nFinancial Analysis\n-----------------------------------\n"
    f"Total Months: {len(list(months))}\n"
    f"Total: ${sum(profit_loss)}\n"
    f"Average Change: ${round(sum(changes) / len(changes), 2)}\n"
    f"Greatest Increase in Profits: {months[25]} (${max(changes)})\n"
    f"Greatest Decrease in Profits: {months[44]} (${min(changes)})\n")

print(Output)


with open(analysis, "w") as output_file:
    output_file.write(Output)

                        
