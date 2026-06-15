# Write your solution here
def greatest_number(a,b,c):
    if a > b:
        if a > c:
            return a
        return c
    else:
        if b > c:
            return b
        return c
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(99, 104, 8)
    print(greatest)
