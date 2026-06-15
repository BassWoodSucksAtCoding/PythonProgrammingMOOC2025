# Write your solution here
hourlyWage = float(input("Hourly wage: "))
hoursWorked = int(input("Hours worked: "))
day = str(input("Day of the week: "))
total = hourlyWage * hoursWorked

if day == "Sunday":
    total = total * 2

print(f"Daily wages: {total} euros")
