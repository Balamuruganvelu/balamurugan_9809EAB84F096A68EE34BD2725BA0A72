class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f"{self.name} is playing cricket.")

class Batsman(Player):
    def __init__(self, name, age, runs_scored):
        super().__init__(name, age)
        self.runs_scored = runs_scored

    def play(self):
        print(f"{self.name} is a batsman and is batting. Runs scored: {self.runs_scored}")

class Bowler(Player):
    def __init__(self, name, age, wickets_taken):
        super().__init__(name, age)
        self.wickets_taken = wickets_taken

    def play(self):
        print(f"{self.name} is a bowler and is bowling. Wickets taken: {self.wickets_taken}")

# Create objects of Player, Batsman, and Bowler
player1 = Player("John", 25)
batsman1 = Batsman("Smith", 30, 56)
bowler1 = Bowler("David", 28, 3)

# Call the play() method for each object
player1.play()
batsman1.play()
bowler1.play()
