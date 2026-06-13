print("Welcome to the Treasure Island.Your mission is to find the treasure")

which_way = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")

if which_way == "left":
    lake_options = input("You've come to a lake. There is an island in the middle of the lake. "
                         "Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    if lake_options == "wait":
        door_options = input("You arrive at the island unharmed. There is a house with 3 doors."
                             "One red, one yellow and one blue. Which colour do you choose?")
        if door_options == "yellow":
            print("You Win!")
        elif door_options =="red":
            print("Its a room full of fire.Game Over.")
        elif door_options == "blue":
            print("room of beasts.Game Over.")
        else:
            print("you chose a door that does not exist.Game Over")
    else:
        print("you got attacked by an angry trout.Game Over.")
else:
    print("you fell in a hole.Game Over.")