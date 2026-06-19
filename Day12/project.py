#Number guessing game
'''

'''

print("Welcome to the Number Guessing Game!\n I am thinking of a number between 1 and 100.")
choose_difficulty =input("Choose a difficulty. Type 'easy' or 'hard':")
attempts = 10 if choose_difficulty == "easy" else 5
#need to change correct_ans based on choose_difficulty
correct_ans = 100 if choose_difficulty == "easy" else 68

def number_guess(correct_ans,attempts):
    while attempts >0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess"))
        if guess < correct_ans:
            print(f"Too low\nGuess again.")
        elif guess > correct_ans:
            print(f"Too high\n Guess again.")
        else:
            print(f"You got it! The answer was {correct_ans}")

        attempts-=1
    return None


number_guess(correct_ans=correct_ans,attempts=attempts)

