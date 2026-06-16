# Write your solution here
def everything_reversed(list_f):
    new_list_f = []

    for i in range(len(list_f)-1,-1,-1):
        row = list_f[i]
        new_list_f.append(row[::-1])

    return new_list_f

