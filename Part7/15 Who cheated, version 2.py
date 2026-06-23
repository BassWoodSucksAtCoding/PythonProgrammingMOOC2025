# Write your solution here
# Write your solution here

import csv
from datetime import datetime

def final_points():

    people = {}
    cheaters = []

    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            people[line[0]] = {}
            people[line[0]]["Final Grade"] = 0
            people[line[0]]["Start time"] = start_time

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")

            if line[0] in people:
                difference = end_time - people[line[0]]["Start time"]
                if difference.seconds > (3600 * 3):
                    continue            

            if int(line[1]) not in people[line[0]] :
                people[line[0]][int(line[1])] = int(line[2])
                people[line[0]]["Final Grade"] += int(line[2])
            elif int(line[2]) > people[line[0]][int(line[1])]:
                people[line[0]]["Final Grade"] -= people[line[0]][int(line[1])]
                people[line[0]][int(line[1])] = int(line[2])
                people[line[0]]["Final Grade"] += int(line[2])
        

    final_grade = {}
    for key,values in people.items():
        final_grade[key] = values["Final Grade"]
    
    return final_grade



