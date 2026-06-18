# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    index = people[0][0]
    for tuple_name in people:
        if tuple_name[1] < oldest:
            oldest = tuple_name[1]
            index = tuple_name[0]
            
   
    return index


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [('Arthur', 1977), ('Emily', 2014)]

    print(oldest_person(people))
