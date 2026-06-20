# Write your solution here
def filter_solutions():
    with open("correct.csv","w") as my_file:
        pass

    with open("incorrect.csv","w") as my_file:
        pass

    with open("solutions.csv") as my_file:
        for line in my_file:
            parts = line.strip().split(";")
            problem = parts[1]
            
            result = parts[2]
            correct = False

            if problem.find("+") != -1:
                operands = problem.split("+")
                correct = (int(operands[0]) + int(operands[1]) == int(result))
            else:
                operands = problem.split("-")
                correct = (int(operands[0]) - int(operands[1]) == int(result))
            
            
            if correct:
                with open("correct.csv","a") as my_file:
                    my_file.write(line)
            else:
                with open("incorrect.csv","a") as my_file:
                    my_file.write(line)

