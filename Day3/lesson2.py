#logical operators

'''
if condiiton 1 and condition 2:
do a
elif condition 1 or condition 2:
do b
'''
print("Welcome to the rollercoaster")
height = int(input("Enter height in cm"))
bill = 0;

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter age"))
    if age <=12:
        bill = 5
        print(f"Child ticket is ${bill}")
    elif age <=18:
        bill = 7
        print(f"Teen ticket is ${bill}")
    elif age>=45 and age <=55:
            print("The ride is on us")
    else:
        bill = 12
        print(f"Adult ticket is ${bill}")

    photo_needed = input("Do you want a photo taken? Type y for Yes and n for No.")
    if photo_needed == 'y':
        bill +=3

    print(f"Your final bill is {bill}")

else:
    print("Not allowed to ride the rollercoaster")

