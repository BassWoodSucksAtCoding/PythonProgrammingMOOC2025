# Write your solution here
from difflib import get_close_matches

text = input("Write text: ")
split_text = text.split(" ")
recovered_text = ""
words = []
wrong_words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())
for word in split_text:
    if word.lower() not in words:
        recovered_text += f"*{word}* "
        wrong_words.append(word)
    else:
        recovered_text += f"{word } "

print(recovered_text)
print("suggestions: ")
for word in wrong_words:
    suggestions = get_close_matches(word,words)
    suggestion_string = ""
    for item in suggestions:
        suggestion_string += f"{item}, "

    print(f"{word}: {suggestion_string[:-2]}")
