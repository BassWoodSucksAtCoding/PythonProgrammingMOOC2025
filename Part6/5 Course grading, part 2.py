# write your solution here
# write your solution here

def file_reader(file_name):
    with open(file_name) as new_file:
        dict_local = {}
        for line in new_file:
            line = line.replace("\n","")
            parts = line.split(";")

            if parts[0] == "id":
                continue

            if file_name == student_info:
                dict_local[parts[0]] = f"{parts[1]} {parts[2]}"
            else:
                dict_local[parts[0]] = 0

                for i in range(1,len(parts)):
                    dict_local[parts[0]] += int(parts[i])
    return dict_local

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_points = "exam_points2.csv"


names = {}
names = file_reader(student_info)

total_exercises = {}
total_exercises = file_reader(exercise_data)

total_exam_points = {}
total_exam_points = file_reader(exam_points)

overall_total_points = {}
grade = {}

for key, values in total_exercises.items():
    percentage = total_exercises[key] / 40 * 100
    bonus_exercise_points = percentage // 10
    overall_total_points[key] = total_exam_points[key] + bonus_exercise_points
            
for key, values in overall_total_points.items():
    if values >= 28:
        grade[key] = 5
    elif values >= 24:
        grade[key] = 4
    elif values >= 21:
        grade[key] = 3
    elif values >= 18:
        grade[key] = 2
    elif values >= 15:
        grade[key] = 1
    else:
        grade[key] = 0

for key, values in grade.items():
    print(f"{names[key]} {values}")
        

# for key, values in names.items():
#     if key in total_exercises:
#         print(f"{names[key]} {total_exercises[key]}")
#     else:
#         print(f"{names[key]} 0")

