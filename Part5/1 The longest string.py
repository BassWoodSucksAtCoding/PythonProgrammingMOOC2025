# Write your solution here
def longest(my_list_local):
    longest_local = len(my_list_local[0])
    longest_index_local = ""

    for item in my_list_local:
        if len(item) > longest_local:
            longest_local = len(item)
            longest_index_local = item
    
    return longest_index_local


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
