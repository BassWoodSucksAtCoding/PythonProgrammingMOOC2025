# Write your solution here

alphabets = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

layer = int(input("Layer: "))
width = layer*2 - 1

new_list = [alphabets[layer-1]] * layer
letter_count = 0

switch = True


for row in range(width):
    for letter in range(len(new_list)-1):
        print(new_list[letter],end="")
    
    for letter in range(len(new_list)-1,-1,-1):
        print(new_list[letter],end="")
    
    print()

    letter_count += 1 

    if alphabets[layer-1-letter_count] != "Z" and switch:
        for i in range(layer-1,letter_count-1,-1):
            new_list[i] = alphabets[layer-1-letter_count]  
    else:
        if switch:
            switch = False
            letter_count = 1
        for i in range(layer-1,layer-letter_count-1,-1):
            new_list[i] = alphabets[letter_count]  
        

    


