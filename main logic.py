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

#The function that writes the new times to the CSV
def CSVWriteFunc(y, x, TimeNeeded):
    NewTimeList = TimeList
    x += 1
    NewTimeList[y][x] = float(NewTimeList[y][x]) + TimeNeeded
    with open("Time Allocations.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(NewTimeList)

# here we GOOOOO
flt_Temp = 0

# BIG Note : When other tasks are inputted the HoursLeft system will have to be overhauled slightly to add the 
# hours of all the tasks. 

for i in range(1, len(TimeList)): #repeat the amount of times = to the number of tasks - i is the task i am on
    HoursLeft = []
    int_TimeNeeded = int(TaskList[i*3]) #Time needed on the first task || This part needs elegancy when intergrated
    for m in range(1, 15): # m is determining the hours left
        flt_Temp = float(TimeList[i][m])
        HoursLeft.append(2 - flt_Temp)
        flt_Temp = 0
    for j in range(0, 14):
        #Somewhere here i need to add a check to make sure the csv isnt too clogged for the time needed to fill it to the maximum
        if int_TimeNeeded == 0:
            pass
        else:
            #If the current date already has 2 hours of tasks, don't use 
            if HoursLeft[j] == 0:
                pass
            elif int_TimeNeeded >= 7 and HoursLeft[j] >= 0.5:
                if HoursLeft[j] == 2:
                    int_TimeNeeded -= 2
                    CSVWriteFunc(i, j, 2)
                else:
                    if HoursLeft[j] >= 1:
                        int_TimeNeeded -= 1
                        CSVWriteFunc(i, j, 1)
                    else:
                        int_TimeNeeded -= 0.5
                        CSVWriteFunc(i, j, 0.5)
            elif j < 3 and HoursLeft[j] >= 0.5:
                if int_TimeNeeded == 0.5:
                    int_TimeNeeded -= 0.5
                    CSVWriteFunc(i, j, 0.5)
                else:
                    if int_TimeNeeded >= 2:
                        if HoursLeft[j] == 2:
                            int_TimeNeeded -= 2
                            CSVWriteFunc(i, j, 2)
                        else:
                            if HoursLeft[j] >= 1:
                                int_TimeNeeded -= 1
                                CSVWriteFunc(i, j, 1)
                            else:
                                int_TimeNeeded -= 0.5
                                CSVWriteFunc(i, j, 0.5)
                    else:
                        if int_TimeNeeded >= 1:
                            if HoursLeft[j] >= 1:
                                int_TimeNeeded -= 1
                                CSVWriteFunc(i, j, 1)
                            else:
                                int_TimeNeeded -= 0.5
                                CSVWriteFunc(i, j, 0.5)
                        #we dont need an else statement here as we already checked above if int_TimeNeeded == 0.5
            elif HoursLeft[j] == 2:
                if int_TimeNeeded >= 2:
                    int_TimeNeeded -= 1
                    CSVWriteFunc(i, j, 1)
                else:
                    if int_TimeNeeded >= 1:
                        int_TimeNeeded -= 1
                        CSVWriteFunc(i, j, 1)
                    else:
                        int_TimeNeeded -= 0.5
                        CSVWriteFunc(i, j, 0.5) 
            elif HoursLeft[j] >= 1:
                if int_TimeNeeded >= 1:
                    int_TimeNeeded -= 0.5
                    CSVWriteFunc(i, j, 0.5)
                else:
                    int_TimeNeeded -= 0.5
                    CSVWriteFunc(i, j, 0.5)
            elif HoursLeft[j] == 0.5:
                int_TimeNeeded -= 0.5
                CSVWriteFunc(i, j, 0.5)

if int_TimeNeeded > 0:
    print("my friend, you have messed up")









