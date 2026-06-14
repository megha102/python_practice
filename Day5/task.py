import random

letters_list = ['a','b','c','d','e','f','g','h'
,'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols_list = ['!','@','#','$','%','^','&','&','*','(',')','+','-',',']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the PyPassword Generator!How many letters would you like in your password?")
n_letters = int(input("How many letters would you like in your password?"))
n_symbols = int(input("How many symbols would you like?"))
n_numbers = int(input("How many numbers would you like?"))

#easy version
#4 letters, 2 symbols and 3 numbers, password = fgdx$*924

# password = ""
#
# for char in range(1,n_letters + 1):
#     random_char = random.choice(letters_list)
#     password += random_char
#
# for num in range(1, n_numbers+1):
#     random_num = random.choice(numbers_list)
#     password += random_num
#
# for symbol in range(1, n_symbols+1):
#     random_symbol = random.choice(symbols_list)
#     password += random_symbol
#
# print(password)

#hard version
#password has no pattern, the positions of symbols, numbers and letters are always changing

password2 = ""
password2_list = []
# combined_list = letters_list + numbers_list + symbols_list

for char in range(1,n_letters + 1):
    random_char = random.choice(letters_list)
    password2_list += random_char

for num in range(1, n_numbers+1):
    random_num = random.choice(numbers_list)
    password2_list += random_num

for symbol in range(1, n_symbols+1):
    random_symbol = random.choice(symbols_list)
    password2_list += random_symbol

random.shuffle(password2_list)
password2 = "".join(password2_list)

print(password2)


