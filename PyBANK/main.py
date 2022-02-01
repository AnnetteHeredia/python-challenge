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
# Started the context manager see mainpoll.py for example. 
# with open (path,"r") as file2:
#     csv_reader = reader(file2, delimiter=",")

#     header = next(csv_reader)


#determine total of months count them all, what is size of data
total_months = len(data)
net_amount = 0
profit_loss_column = []

for row in data:
    #net_amount = net_amount + in(row[1])
    net_amount += int(row[1])
    profit_loss_column.append(int(row[1]))

#average_change = round((net_amount / total_months),2)

#the greatest increase in profits
greatest_inc = max(profit_loss_column)
date_inc = data[profit_loss_column.index(greatest_inc)][0]
greatest_dec = min(profit_loss_column)
date_dec = [profit_loss_column.index(greatest_dec)] [0]

#output
print(f"Financial Analysis")
print(f"-"*28)
print(f"Total Months: {total_months}")
print(f"Total : ${net_amount}")
print(f"Greatest Increase in Profits: {date_inc} (${greatest_inc}) ")
print(f"Greatest Decrease in Profits: {date_dec}(${greatest_dec}")


f = open("Pybankdata.txt",'w')
f.write("Financial Analysis\n")
f.write(f"-28")
f.write("\n")
f.write(f"Total Months : {total_months}\n")
f.write(f"Total : ${net_amount}")
f.write(f"Greatest Increase in Profits: {date_inc} (${greatest_inc})")
f.write(f"Greatest Decrease in Profits: {date_dec} (${greatest_dec})")
f.close()