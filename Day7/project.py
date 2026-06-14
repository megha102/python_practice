#HANGMAN
import random

words_list = ["python", "developer", "airport", "guitar", "science", "ocean"]

random_word = random.choice(words_list)
random_word_length = len(random_word)

random_word_to_guess = ""
for i in range(0,random_word_length):
    random_word_to_guess += "_"

print(f"Word to guess: {random_word_to_guess}")

your_guess = input("guess a letter:")
lives = 6

random_word_list = list(random_word_to_guess)
found = False

# print(len(random_word_to_guess))
# print(len(random_word_list))

while lives > 1:
    for i in range(len(random_word)):
        if random_word[i]==your_guess and not(your_guess in random_word_list):
            found = True
            random_word_list[i] = your_guess
            print(f"The word now is: {''.join(random_word_list)}")
            break
        else:
            found = False

    if not found:
        print(f"you guessed {your_guess}, that's not in the word. You lose a life")
        lives-=1
        print(f"{lives}/6 left")

    your_guess = input("guess a letter again")

print(f"The word was: {random_word}")



