
import os
import csv
csvpath = os.path.join("PyBank/budget_data.csv")

total_months = []
total_profit = []
profit_change = []

with open(csvpath,newline="", encoding="utf-8") as budget_outcome:
    csvreader = csv.reader(budget_outcome,delimiter=",") 
    csv_header = next(budget_outcome)
    print(f"Header: {csv_header}")

    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = os.path.join("PyBank", "Budget_Summary.txt")

with open(output_file,"w") as file:
    
    file.write("Budget Summary")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
