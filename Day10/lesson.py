#function with outputs
"""def my_func():
    result = 3*2
    return result

print(4+my_func())"""

def format_name(f_name, l_name):
    full_name = f_name.title() + " " + l_name.title()
    return full_name

print(format_name("megha","gulati"))

def function_1(text):
    return text+text

def function_2(text):
    return text.title()

print(function_2(function_1("hello")))

#function with more than 1 output
def format_name(f_name,l_name):
    """
    #docstrings - documentation for the functions that we write.
    :param f_name: first name
    :param l_name: last name
    :return: the title case version of the name.
    """
    if f_name == " " or l_name == " ":
        return None
    return f"{f_name.title()} {l_name.title()}"

print(format_name(input("Enter first name"), input("Enter last name")))

def outer_func(a,b):
    def inner_func(c,d):
        return c+d
    return inner_func(a,b)

print(outer_func(5,10))


