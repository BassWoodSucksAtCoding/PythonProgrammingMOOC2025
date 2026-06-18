# Write your solution here
def create_tuple(x: int, y: int, z: int):
    new_list = [x,y,z]
    new_list.sort()
    new_tuple = (new_list[0],new_list[2],x+y+z)
    return new_tuple



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
