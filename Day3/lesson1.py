'''
if condition:
do a
elif condition:
do b
else:
do c

= assignment
== comparison
'''
print("Welcome to the rollercoaster")
height = int(input("Enter height in cm"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter age"))
    if age <=12:
        bill = 5
        print(f"Child ticket is ${bill}")
    elif age <=18:
        bill = 7
        print(f"Teen ticket is ${bill}")
    else:
        bill = 12
        print(f"Adult ticket is ${bill}")

    photo_needed = input("Do you want a photo taken? Type y for Yes and n for No.")
    if photo_needed == 'y':
        bill +=3

    print(f"Your final bill is {bill}")

else:
    print("Not allowed to ride the rollercoaster")


'''
Modulo % operator
10%5 = 0 -> no remainder
10%3 = 3 -> 1 remainder
'''

#check odd/even number
num = int(input("Enter number"))
if num%2 == 0:
    print("even")
else:
    print("odd")

