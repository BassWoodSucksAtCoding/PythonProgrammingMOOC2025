# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_dict_local = {}
    new_dict_local["name"] = name
    new_dict_local["director"] = director
    new_dict_local["year"] = year
    new_dict_local["runtime"] = runtime

    database.append(new_dict_local)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
