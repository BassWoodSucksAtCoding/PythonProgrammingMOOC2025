# Write your solution here
editor = ""
while editor != "visual studio code":
    editor = input("Editor: ").lower()
    
    if editor == "visual studio code":
        print("an excellent choice!")
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
