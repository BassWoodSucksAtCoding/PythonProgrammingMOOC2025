# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            prices = float(parts[1])
            fruits[name] = prices
        
    return fruits

