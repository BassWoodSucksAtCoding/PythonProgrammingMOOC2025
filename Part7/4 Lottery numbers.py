# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    random_numbers = list(range(lower,upper+1))
    return sorted(sample(random_numbers,amount))
    
