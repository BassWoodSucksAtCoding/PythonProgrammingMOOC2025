# Write your solution here
def search_by_ingredient(filename: str, ingredient: str):
    recipe_dict = dictionary_converter(filename)
    found_recipes = []

    for key, values in recipe_dict.items():
        
        ingredient = ingredient.lower()

        for item in values:
            helper_var = item.lower
            if item.find(ingredient) != -1:
                found_recipes.append(f"{key}, preparation time {values[0]} min")
    
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    recipe_dict = dictionary_converter(filename)
    found_recipes = []

    for key, values in recipe_dict.items():
        if int(values[0]) <= prep_time:
            found_recipes.append(f"{key}, preparation time {values[0]} min")
    
    return found_recipes

def search_by_name(file_name,search_item):
    recipe_dict = dictionary_converter(file_name)
    found_recipes = []

    for key, values in recipe_dict.items():
        helper_var = key.lower()
        search_item = search_item.lower()
        if helper_var.find(search_item) != -1:
            found_recipes.append(key)
    
    return found_recipes


def dictionary_converter(file_name):
    recipe = {}
    start = True
    key = ""
    with open(file_name) as new_file:
        for line in new_file:
            line = line.strip()
            if start:
                key = line
                recipe[key] = []
                start = False
            elif line == "":
                start = True
            else:
                recipe[key].append(line)
    
    return recipe
            


# print(search_by_name("recipes1.txt", "cake"))

# found_recipes = search_by_name("recipes2.txt", "oat")

# for recipe in found_recipes:
#     print(recipe)

# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)
