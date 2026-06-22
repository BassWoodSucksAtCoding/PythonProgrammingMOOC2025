# Write your solution here
from datetime import datetime 

def is_it_valid(pic: str):
    control = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    day = int(f"{pic[0]}{pic[1]}")
    month = int(f"{pic[2]}{pic[3]}")
    year = int(f"{pic[4]}{pic[5]}")
    personal = int(f"{pic[7]}{pic[8]}{pic[9]}")

    if len(pic) != 11:
        return False
        
    if day < 1 or day > 31:
        return False

    if month < 1 or month > 12:
        return False
    
    if year <= 0 and pic[6] != "A":
        return False

    if not(pic[6] == "-" or pic[6] == "+" or pic[6] == "A"):
        return False
    
    digit = int(f"{pic[0]}{pic[1]}{pic[2]}{pic[3]}{pic[4]}{pic[5]}{pic[7]}{pic[8]}{pic[9]}")


    index = digit % 31

    if pic[10] != control[index]:
        return False
    
    return True

