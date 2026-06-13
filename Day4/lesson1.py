#Randomisation

'''
python uses mersenne twister - pseudorandom number generators in khan academy
random is python module - large code with multiple functions-> module and then use that module
'''

import random

#random number between the interval 34 and 89
print(random.randint(34,89))

#next random floating point number in the range 0.0 <= X<=1.0
random_number_0_to_1 = random.random() * 10
print(round(random_number_0_to_1,2))

#random.uniform(a,b) return random floating point number N such that N in [a,b]
random_number_between_two_values = random.uniform(41,500)
print(random_number_between_two_values)

toss_result = random.randint(0,1)

if toss_result == 1:
    print("Heads")
else:
    print("Tail")