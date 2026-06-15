# Write your solution here
def same_chars(text,a,b):
    if b > len(text)-1 or a > len(text)-1:
        return False

    if text[a] == text[b]:
        return True
    return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
