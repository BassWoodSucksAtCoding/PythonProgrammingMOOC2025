# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        numbers_list = []
        for line in new_file:
            numbers_list.append(int(line))
        
        return max(numbers_list)


