# Write your solution here
import string, operator

def run(program):
    variables = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }

    operation_converter = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le
    }

    lines_of_code = len(program) - 1
    current_line = 0
    end = False

    print_commands = []
    locations = {}

    for i in range(len(program)):
        if program[i][0].islower():
            locations[program[i][:-1]] = i
            
    while current_line <= lines_of_code and not end:
        operation = program[current_line].split(" ")

        if operation[0] == "PRINT":
            print_commands.append(int(operation[1]) if operation[1].isdigit() else variables[operation[1]])

        elif operation[0] == "MOV":
            variables[operation[1]] = int(operation[2]) if operation[2].isdigit() else variables[operation[2]]
        
        elif operation[0] == "ADD":
            variables[operation[1]] += int(operation[2]) if operation[2].isdigit() else variables[operation[2]]
                    
        elif operation[0] == "SUB":
            variables[operation[1]] -= int(operation[2]) if operation[2].isdigit() else variables[operation[2]]
        
        elif operation[0] == "MUL":
            variables[operation[1]] *= int(operation[2]) if operation[2].isdigit() else variables[operation[2]]
        
        elif operation[0] == "JUMP":
            if operation[1] in locations:
                current_line = locations[operation[1]] - 1
        
        elif operation[0] == "IF":
            # 0    1          2          3      4      5
            # IF [value] [comparison] [value] JUMP [location]
            value1 = int(operation[1]) if operation[1].isdigit() else variables[operation[1]]
            value2 = int(operation[3]) if operation[3].isdigit() else variables[operation[3]]

            if operation_converter[operation[2]](value1,value2):

                if operation[5] in locations:

                    current_line = locations[operation[5]]
  
        elif operation[0] == "END":
            end = True
        
        else:
            locations[operation[0][:-1]] = current_line

        current_line += 1

    return print_commands

