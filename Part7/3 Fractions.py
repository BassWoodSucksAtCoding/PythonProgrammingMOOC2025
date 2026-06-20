# Write your solution here
import fractions
def fractionate(amount: int):
    fraction_list = []
    for i in range(amount):
        fraction_list.append(fractions.Fraction(1,amount))
    
    return fraction_list


# for p in fractionate(3):
#     print(p)

# print()

# print(fractionate(5))
