# Write your solution here
def most_common_character(string_f):
    most_common_f = 0
    most_common_letter_f = ""
    for letter in string_f:
        if string_f.count(letter) > most_common_f:
            most_common_f = string_f.count(letter)
            most_common_letter_f = letter
    
    return most_common_letter_f
