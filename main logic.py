#main logic

#We want to prioritise putting tasks ahead and not spreading it out exactly evenly

from datetime import date
from datetime import datetime
import csv

TaskList = []
TimeList =[]
HoursLeft = []

with open("Task List.txt") as fh:
    for line in fh:
        TaskList.append(line.rstrip("\n"))

# EXAMPLE
Task1Date = TaskList[2]
Task1Date_obj = datetime.strptime(Task1Date, '%d/%m/%y')
DaysUntilDue = int(str(Task1Date_obj - datetime.today())[0]) + 1

with open("Time Allocations.csv") as file:
    for i in range(1, 14):
        data = csv.reader(file)
        for row in data:
            TimeList.append(row)

flt_Temp = float(0)

for i in range(1, 15):
    for j in range(1, len(TimeList)):
        flt_Temp += float(TimeList[j][i])
    HoursLeft.append(2 - flt_Temp)
    flt_Temp = float(0)

print(HoursLeft)






