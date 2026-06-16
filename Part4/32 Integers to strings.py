def formatted(my_list):
    new_list = []

    for number in my_list:
        new_list.append(f"{number:.2f}")

    return new_list
