#there is no block scope in python

enemies = ["zombies", "vampires", "warewolves"]
game_level = 3

#we can still use new_enemy outside if/while/for block
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

#we cant use new_enemy outside function
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

#Global Constants: variables which you define and you are never planning on changing it over again.
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

