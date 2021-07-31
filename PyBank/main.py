import csv
import os

# Load files
load_file = os.path.join("PyBank", "Resources", "budget_data.csv")
output_file = os.path.join("PyBank", "Analysis", "Text File")

# Financial tracker
months_in_total = 0
month_change = []
netChange_list = []
greatestIncrease = ["", 0]
greatDecrease = ["", 9999999999999999]
net_total = 0

# Read the csv and make dictionaries
with open(load_file) as financial_data:
  reader = csv.reader(financial_data)

  header = next(reader)

  first_row = next(reader)
  months_in_total += 1
  net_total += int(first_row[1])
  previous_net = int(first_row[1])

  for row in reader:

    months_in_total += 1
    net_total += int(row[1])

    net_change = int(row[1]) - previous_net
    previous_net = int(row[1])
    netChange_list +=[net_change]
    month_change += [row[0]]

    if net_change > greatestIncrease[1]:
      greatestIncrease[0] = row[0]
      greatestIncrease[1] = net_change

    if net_change < greatDecrease[1]:
      greatDecrease[0] =row[0]
      greatDecrease[1] = net_change

monthly_net_average = sum(netChange_list) / len(netChange_list)

output = (
  f"Finanlcial Analysis\n"
  f"---------------------\n"
  f"Total Months: {months_in_total}\n"
  f"Total: ${net_total}\n"
  f"Average Change: ${monthly_net_average:.2f}\n"
  f"Greatest Increase in Profits: {greatestIncrease[0]}(${greatestIncrease[1]})\n"
  f"Greatest Decrease in Profits: {greatDecrease[0]}(${greatDecrease[1]})\n")

print(output)
with open(output_file, "w") as txt_file:
  txt_file.write(output)