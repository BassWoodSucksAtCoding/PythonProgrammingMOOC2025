# Copy here code of line function from previous exercise and use it in your solution
def line(times, text):
    if text == "":
        print("*"*times)
    else:
        print(text[0]*times)

def shape(triangle_height,triangle_character,rectangle_height,rectangle_character):
    for row in range(1,triangle_height+1):
        line(row, triangle_character)
    
    for row in range(1,rectangle_height+1):
        line(triangle_height,rectangle_character)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "*")
