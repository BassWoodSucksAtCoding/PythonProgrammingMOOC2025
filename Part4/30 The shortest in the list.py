# Write your solution here

# Write your solution here

def shortest(my_list):
    longest = len(my_list[0])
    index = 0
    for i in range(len(my_list)):
        if len(my_list[i]) < longest:
            longest = len(my_list[i])
            index = i
    
    return my_list[index]
