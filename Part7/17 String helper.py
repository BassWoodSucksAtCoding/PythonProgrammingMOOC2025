# Write your solution here
import string
def change_case(orig_string: str):
    new_string = ""
    for letter in orig_string:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    
    return new_string

def split_in_half(orig_string: str):
    length = len(orig_string)
    half = length // 2
    return (orig_string[:half],orig_string[half:])

def remove_special_characters(orig_string: str):
    valid = " "
    valid += string.ascii_lowercase
    valid += string.ascii_uppercase
    valid += string.digits

    new_string = ""
    for letter in orig_string:
        if letter not in valid:
            continue
        else:
            new_string += letter
            
    return new_string

