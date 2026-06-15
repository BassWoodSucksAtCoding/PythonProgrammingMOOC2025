# Copy here code of line function from previous exercise

def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def box_of_hashes(height):
    # You should call function line here with proper parameters
    for row in range(height):
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
