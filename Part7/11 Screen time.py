# Write your solution here
from datetime import datetime, timedelta

file_name = input("Filename: ")
with open(file_name,"w") as new_file:
    starting_date = input("Starting date: ")
    starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
    days = int(input("How many days: "))
    times = {}
    total = 0

    print("Please type in screen time in minutes on each day (TV computer mobile):")
    for i in range(days):
        my_time = starting_date + timedelta(days=i)
        minutes = input(f"Screen time {my_time.strftime("%d.%m.%Y")}:")
        times[my_time.strftime("%d.%m.%Y")] = minutes.replace(" ", "/")
        minutes = minutes.split(" ")
        for minute in minutes:
            total += int(minute)
    
    new_file.write(f"Time period: {starting_date.strftime("%d.%m.%Y")}-{(starting_date + timedelta(days=days-1)).strftime("%d.%m.%Y")}\n")
    new_file.write(f"Total minutes: {total}\n")
    new_file.write(f"Average minutes: {total/days}\n")

    for key,values in times.items():
          new_file.write(f"{key}: {values}\n")

    print(f"Data stored in file {file_name}")      


        
    
