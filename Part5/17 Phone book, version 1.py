# Write your solution here

contacts = {}
End = True

while End:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("no number")
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        contacts[name] = number
        print("ok!")
    elif command == 3:
        print("quitting...")
        End = False
