#calculator app
'''
user input : enter number1
show operators
user input: pick an operator
user input: next number2

print: number1 operator number2 + result
print: type 'y' to continue calculating with result or
type 'n' to start a new calculation.
'''

def calculate(num1, num2, operator):
    if operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1/num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return abs(num1 - num2)
    else:
        return "Invalid Operator"

num1 = float(input("Enter number 1"))
operator = input("pick operator from:\n *\n/\n+\n-")
num2 = float(input("Enter number 2"))

result = calculate(num1,num2,operator)
print(f"{num1}{operator}{num2} = {result}")
choice = input("type 'y' to continue calculating with result or type 'n' to start a new calculation")

while choice:
    while choice != 'n':
        num = float(input("Enter number"))
        operator2 = input("pick operator from:\n *\n/\n+\n-")
        result2 = calculate(num, result, operator2)
        print(f"{num}{operator2}{result} = {result2}")

    while choice != 'y':
        num2 = float(input("Enter number 1"))
        operator3 = input("pick operator from:\n *\n/\n+\n-")
        num3 = float(input("Enter number 2"))

        result3 = calculate(num2, num3, operator3)
        print(f"{num2}{operator3}{num3} = {result3}")
