# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = [0]

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers) - 1
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        length = self.count_numbers()
        if length == 0:
            return 0
        else:
            return self.get_sum() / length


stats = NumberStats()
odd = NumberStats()
even = NumberStats()
while True:
    print("Please type in integer numbers:")
    number = int(input())

    if number != -1:
        if number % 2 == 0:
            even.add_number(number)
        else:
            odd.add_number(number)
        stats.add_number(number)
    else:
        break

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")
