#Lists
'''
list is a data structure - hard to keep track of so many variables and DS useful in case
of any relationship between data points.
list:
fruit = [item1, item2]
'''

#save 50 states
states_of_India = ['Mumbai', 'Delhi','Kolkata','Bengaluru']
states_of_India[1] = 'New Delhi'

# print(states_of_India)

states_of_India.append('Hyderabad')

# print(states_of_India)
states_of_India.extend(['Gujarat', 'UP'])
# print(states_of_India)

#read documentation

# IndexOutOfRange
number_states = len(states_of_India)
# print(states_of_India[number_states-1])

# dirty_dozen = ['strawberries', 'spinach', 'apples', 'grapes', 'kale', 'cherries']

#nested lists
fruits = ['apples','cherries','grapes','strawberries']
veg = ['spinach','kale']

dirty_dozen = [fruits, veg]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][1]) #kale -> go to 1st index of dirty_dozen -> u found a list now go to 1st index of that list