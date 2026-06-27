# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def tick(self):
        self.seconds += 1
        if self.seconds > 59:
            self.minutes += 1
            self.seconds = 0

            if self.minutes > 59:
                self.minutes = 0
                self.seconds = 0
    
    def __str__(self):
        if self.minutes < 10:
            minutes = f"0{self.minutes}"
        else:
            minutes = self.minutes

        if self.seconds < 10:
            seconds = f"0{self.seconds}"
        else:
            seconds = self.seconds
        
        return f"{minutes}:{seconds}"


# watch = Stopwatch()
# for i in range(120):
#     print(watch)
#     watch.tick()


