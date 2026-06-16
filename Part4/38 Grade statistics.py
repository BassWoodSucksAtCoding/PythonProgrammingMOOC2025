# Write your solution here

overall_total_points = 0
percentage_passed = 0
students = 0
overall_grades = [0,0,0,0,0,0]

while True:
    exam_point = input("Exam points and exercises completed: ")

    if exam_point != "":
        students += 1
        result = exam_point.split()
        
        result[0] = int(result[0])
        result[1] = int(result[1])

        if result[1] < 10:
            individual_total_points = result[0]
        else:
            individual_total_points = result[1] // 10 + result[0]
        
        if result[0] < 10:
            grade = 0
            overall_grades[0] += 1
        else:
            
            if individual_total_points >= 28 and individual_total_points <= 30:
                grade = 5
                overall_grades[5] += 1
            elif individual_total_points >= 24 and individual_total_points <= 27:
                grade = 4
                overall_grades[4] += 1
            elif individual_total_points >= 21 and individual_total_points <= 23:
                grade = 3
                overall_grades[3] += 1
            elif individual_total_points >= 18 and individual_total_points <= 20:
                grade = 2
                overall_grades[2] += 1
            elif individual_total_points >= 15 and individual_total_points <= 17:
                grade = 1
                overall_grades[1] += 1
            else:
                grade = 0
                overall_grades[0] += 1
            
        
        if grade > 0:
            percentage_passed += 1
        
        overall_total_points += individual_total_points

    else:
        break



overall_average_points = overall_total_points/students
percentage_passed = percentage_passed/students * 100

print("Statistics: ")
print(f"Points average: {overall_average_points:.1f}")
print(f"Pass percentage: {percentage_passed:.1f}")
print(f"Grade distribution:")
for i in range(5,-1,-1):
    print(f"  {i}: " + "*"*overall_grades[i])
