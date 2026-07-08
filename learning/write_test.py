word = "apple"
number_1 = 20
number_2 = 3

combined = f"{word}, {number_1}, {number_2}"

with open("file.txt", "w") as file:
    file.write(combined)

#class

class Player:
    def __init__(self, player_name, user, age, level):
        self.player_name = player_name
        self.user = user
        self.age = age
        self.level = level

player = Player("Emily", "astroem", 18, 1)
combined = f"{player.player_name}<|> {player.user}<|> {player.age}<|> {player.level}"

with open("player.txt", "w") as file_:
    file_.write(combined)