print("Welcome to the Python pizza deliveries!")
size = input("What size do you want? S, M or L:")
mushrooms = input("Do you want mushrooms on your pizza? Y or N ")
cheese = input("Do you want extra cheese? Y or N")
bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20

else:
    bill = 25

if mushrooms ==  'Y':
    if size == 'S':
        bill += 2
    else:
        bill +=3

if cheese == 'Y':
    bill += 1

print(f"total bill is ${bill}")