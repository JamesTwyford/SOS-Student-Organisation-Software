#main logic

#We want to prioritise putting tasks ahead and not spreading it out exactly evenly

from datetime import date
from datetime import datetime
import csv

TaskList = []
TimeList =[]
HoursLeft = []
NewTimeList = []

with open("Task List.txt") as fh:
    for line in fh:
        TaskList.append(line.rstrip("\n"))

# EXAMPLE
Task1Date = TaskList[2]
obj_Task1Date = datetime.strptime(Task1Date, '%d/%m/%y')
int_DaysUntilDue = int(str(obj_Task1Date - datetime.today())[0])

with open("Time Allocations.csv") as file:
    for i in range(1, 14):
        data = csv.reader(file)
        for row in data:
            TimeList.append(row)

def CSVWriteFunc(y, x, TimeNeeded):
    NewTimeList = TimeList
    x += 1
    NewTimeList[y][x] = float(NewTimeList[y][x]) + TimeNeeded
    with open("Time Allocations.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(NewTimeList)

# here we GOOOOO
flt_Temp = 0

for i in range(1, len(TimeList)): #repeat the amount of times = to the number of tasks - i is the task i am on
    HoursLeft = []
    int_TimeNeeded = int(TaskList[i*3]) #Time needed on the first task
    for m in range(1, 15): # m is determining the hours left
        flt_Temp = float(TimeList[i][m])
        HoursLeft.append(2 - flt_Temp)
        flt_Temp = 0
    for j in range(0, 14):
        if int_TimeNeeded == 0:
            pass
        else:
            if HoursLeft[j] == 0:
                pass
            elif int_TimeNeeded > 10:
                int_TimeNeeded -= 2
                CSVWriteFunc(i, j, 2)
            elif j < 4 and HoursLeft[j] >= 0.5:
                if int_TimeNeeded == 0.5:
                    int_TimeNeeded -= 0.5
                    CSVWriteFunc(i, j, 0.5)
                else:
                    int_TimeNeeded -= 1
                    CSVWriteFunc(i, j, 1)
            elif 14 - j < 3 and HoursLeft[j] == 2:
                if int_TimeNeeded >= 2:
                    int_TimeNeeded -= 2
                    CSVWriteFunc(i, j, 2)s
                else:
                    int_TimeNeeded -= int_TimeNeeded
                    CSVWriteFunc(i, j, int_TimeNeeded)
            elif HoursLeft[j] == 2:
                if int_TimeNeeded >= 2:
                    int_TimeNeeded -= 1
                    CSVWriteFunc(i, j, 1)
                else:
                    if int_TimeNeeded >= 1:
                        int_TimeNeeded -= 1
                        CSVWriteFunc(i, j, 1)
                    else:
                        int_TimeNeeded -= int_TimeNeeded
                        CSVWriteFunc(i, j, int_TimeNeeded)
            elif HoursLeft[j] >= 1:
                if int_TimeNeeded >= 1:
                    int_TimeNeeded -= 0.5
                    CSVWriteFunc(i, j, 0.5)
                else:
                    int_TimeNeeded -= int_TimeNeeded
                    CSVWriteFunc(i, j, int_TimeNeeded)
            elif HoursLeft[j] == 0.5:
                int_TimeNeeded -= 0.5
                CSVWriteFunc(i, j, 0.5)

if int_TimeNeeded > 0:
    print("my friend, you have messed up")









