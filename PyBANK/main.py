#a library to read in csv files'
from csv import reader 
#a library to allow formatting of a directory path
from pathlib import Path 

path = Path("PyBank/Resources/budget_data.csv")
#opened file'
file = open(path)
#convert file to a list.
file = list (reader(file))
#dont start with header just data
data = file[1:]

#determine total of months count them all, what is size of data
total_months = len(data)
net_amount = 0
profit_los_column=[]

for row in data:
    #net_amount = net_amount + in(row[1])
    net_amount += int(row[1])
    profit_loss_column.append(int(row[1]))

#average_change = round

#the greatest increase in profits
greatest_inc = max(profit_loss_column)
date_inc = data[profit_loss_column.index(greatest_inc)][0]
greatest_dec = min(profit_loss_column.index)

#output
print(f"Financial Analysis")
print(f"-*28")
print(f"Total Months: {total_months}")
print(f"Total : $[net_amount")
print(f"Greatest ")



f = open("Pybankdata.txt",'w')
f.write("Financial Analysis\n")
f.write(f"-28")
f.write("\n")
f.write("Total Months : {total_months}\n")

f.close()