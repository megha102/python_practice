#datatypes
#subscripting
print("Hello"[-1])

#String
print("123" + "345") #concatenation

#Integer  = whole number
print(123+345)

#Large integers
print(123_456_789)

#Float = decimal point
print(3.14)

#boolean
print(True)
print(False)

#functions: each function is expected to work with specific datatypes
print(len("12345"))

#type checking
print(type("hek"))
print(type(123))
print(type(True))
print(type(123.45))

print(f"Number of letters in your name:"+str(len(input("enter your name"))))

#operators
print(3-4)
print(6/4)
print(6//4) #removing decimal places
print(2**6)

#BODMAS or #PEMDAS (paranthesis, exponent, multiplication, division, addition, subtraction)

print(3*3+3/3-3)
# 3*3+1-3
# 9+1-3
#10-3
#7

bmi = 84/1.65**2
# print(bmi)
print(int(bmi))
print(round(bmi,2))

score = 0
score +=1
# print(score)

#f-strings
# print(f"your score is {score}")

height = 1.8
is_winning = True
# print(f"your score is {score}, your height is {height}. You are winning is {is_winning}")

