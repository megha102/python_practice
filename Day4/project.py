#Rock, paper and scissor
import random

my_choice = input("Rock, paper, scissor?").lower()

comp_list = ["rock", "paper","scissor"]
comp_choice = random.choice(comp_list)
print(comp_choice)

if my_choice == "rock" and comp_choice == "paper":
    print("computer wins")
elif my_choice == "paper" and comp_choice == "rock":
    print("you win")
elif my_choice == "scissor" and comp_choice == "rock":
    print("computer wins")
elif my_choice == "rock" and comp_choice == "scissor":
    print("you win")
elif my_choice == "scissor" and comp_choice == "paper":
    print("you win")
elif my_choice == "paper" and comp_choice == "scissor":
    print("computer wins")
else:
    print("tie")