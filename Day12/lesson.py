#scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

# drink_potion()
# print(potion_strength) -> only valid within function

#global scope
player_health = 10

def drink():
    print(player_health)

# drink()

#anything that you give name to has a namespace

'''
Modify the global scope 
'''
enemies = 1

# def increase_enemies_2():
#     global enemies #it will tell compiler that we are using the global variable  - not used often - its advised to  not modify global variable inside a function
#     enemies +=1

#then how to use it to change global variable? -> pass it in the function
# def increase_enemies_3(enemy):
#     print(f"enemies inside function {enemy}")
#     return enemy + 1

#then assign it to the global variable
# enemies = increase_enemies_3(enemies)
# print(f"enemies outside function: {enemies}")
