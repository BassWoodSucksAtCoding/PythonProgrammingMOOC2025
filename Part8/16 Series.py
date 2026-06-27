# Write your solution here:
class Series():
    def __init__(self, title, season, genre):
        self.title = title
        self.season = season
        self.genre = genre
        self.rating = []
        self.avg = 0
    
    def rate(self,user_rating):
        self.rating.append(user_rating)
        avg = sum(self.rating) / len(self.rating)
        self.avg = avg
    
    def __str__(self):
        genre_list = self.genre
        genre_string = ", ".join(genre_list)
        if self.rating == []:
            return f"{self.title} ({self.season} seasons) \ngenres: {genre_string} \nno ratings"
        else:

            return f"{self.title} ({self.season} seasons) \ngenres: {genre_string} \n{len(self.rating)} ratings, average {self.avg:.1f} points"

def minimum_grade(rating: float, series_list: list):
    found_series = []
    for series in series_list:
        if series.avg >= rating:
            found_series.append(series)

    return found_series

def includes_genre(genre: str, series_list: list):
    found_series = []
    for series in series_list:
        if genre in series.genre:
            found_series.append(series)
    
    return found_series


        
# s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
# s1.rate(5)

# s2 = Series("South Park", 24, ["Animation", "Comedy"])
# s2.rate(3)

# s3 = Series("Friends", 10, ["Romance", "Comedy"])
# s3.rate(2)

# series_list = [s1, s2, s3]

# print("a minimum grade of 4.5:")
# for series in minimum_grade(4.5, series_list):
#     print(series.title)

# print("genre Comedy:")
# for series in includes_genre("Comedy", series_list):
#     print(series.title)
