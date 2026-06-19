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
            elif file_name == exercise_data:
                dict_local[parts[0]] = 0

                for i in range(1,len(parts)):
                    dict_local[parts[0]] += int(parts[i])
    return dict_local

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"


names = {}
names = file_reader(student_info)

total_exercises = {}
total_exercises = file_reader(exercise_data)

for key, values in names.items():
    if key in total_exercises:
        print(f"{names[key]} {total_exercises[key]}")
    else:
        print(f"{names[key]} 0")

