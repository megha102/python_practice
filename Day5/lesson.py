#for loop
from math import inf

fruits = ['Apple', 'Peach','Pear']

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

student_scores = [75,82,91]
print(sum(student_scores))
sum = 0

for score in student_scores:
    sum += score

print(sum)

print(max(student_scores))
#
max_score = -inf
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#for loops with other data structures
# range(a,b) [a,b)
# range(a,b,c) c-> step the interval between a and b
for number in range(1,11,3):
    print(number)

#Gauss Challenge
s = 0
for num in range(1,101):
    s += num
print(s)

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)