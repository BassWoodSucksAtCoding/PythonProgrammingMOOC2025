# Write your solution here
def asterisk(search_term : str):
    word_list = []
    with open("words.txt") as new_file:
        for line in new_file:
            line = line.strip().lower()
            if search_term[0] == "*":
                if line.endswith(search_term[1:]):
                        word_list.append(line)
            else:
                if line.startswith(search_term[:-1]):
                        word_list.append(line)
    return word_list

def dot(search_term: str):
    with open("words.txt") as new_file:
        word_list = []
        for line in new_file:
            line = line.strip().lower()
            found = True
            
            
            if len(line) == len(search_term):
                for letter_index in range(len(line)):
                    # print(search_term[letter_index])
                    # print(line[letter_index])
                    if search_term[letter_index] == ".":
                        continue
                    elif search_term[letter_index] != line[letter_index]:
                        found = False
                        break
            else:
                found = False
                
            if not found:
                continue
            else:
                word_list.append(line)
    return word_list



def find_words(search_term : str):

    if search_term.find("*") != -1:
        return asterisk(search_term)
    elif search_term.find(".") != -1:
        return dot(search_term)
    else:
        with open("words.txt") as new_file:
            for line in new_file:
                if line.strip().lower() == search_term:
                    return [search_term]


