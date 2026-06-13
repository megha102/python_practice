import random

friends= ['Alice', 'Bob', 'Charlie','David','Emanuel']

#documentation
print(random.choice(friends))

#from what we already know
random_index = random.randint(0,4)
print(friends[random_index])