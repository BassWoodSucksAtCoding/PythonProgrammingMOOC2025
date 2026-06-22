# Write your solution here

import csv
from datetime import datetime

def cheaters():

    people = {}
    cheaters = []

    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            people[line[0]] = ["",""]
            people[line[0]] = (start_time)

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            end_time = datetime.strptime(line[3], "%H:%M")

            if line[0] in people:
                difference = end_time - people[line[0]]
                if difference.seconds > (3600 * 3) and line[0] not in cheaters:
                    cheaters.append(line[0])

    return cheaters


