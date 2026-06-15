# Write your solution here
def all_the_longest(my_list):
    new_list = []
    longest = len(my_list[0])
    for i in range(len(my_list)):
        if len(my_list[i]) > longest:
            longest = len(my_list[i])
            new_list = [my_list[i]]
        elif len(my_list[i]) == longest:
            new_list.append(my_list[i])
    
    return new_list
