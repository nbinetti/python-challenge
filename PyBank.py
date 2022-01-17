import csv
import os

# bring in budget file and analysis text file
budget_data = os.path.join("Resources", "budget_data.csv")
analysis = os.path.join("Analysis", "budget_analysis.txt")

# Financial parameters 
total_months = 0
total_net = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# open the file 
with open(budget_data) as budget1:
    reader = csv.reader(budget1)

# header
    header = next(reader)

# ignore header for change in month for profit/loss 
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track total_months and total_net
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track net_change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate greatest_increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate greatest_decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(analysis, "w") as txt_file:
    txt_file.write(output)


