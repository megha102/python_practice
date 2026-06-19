#Python Object oriented programming

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@abc.com'

        Employee.num_of_employees+=1

    def display_full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


#Classes and Instances
emp1 = Employee( 'corey','shafer',50000)
emp2 = Employee('Test','user',60000)

# print(Employee.num_of_employees)

# print(emp1.display_full_name())
#internally below is called
# print(Employee.display_full_name(emp2))

#Class Variables - why important?
#current case - raise_amount not defined
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

#able to access raise_amount :emp1.raise_amount
#able to update the 4% amount above

#all are 1.04 same
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

#print(emp1.__dict__)
# print(Employee.__dict__)

# emp1.raise_amount = 1.05
# print(emp1.raise_amount)
# print(emp2.raise_amount)

#class method vs normal methods

#currently below will be same -
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

# Employee.set_raise_amt(1.05)
#
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

#class methods example

emp_str1 = 'John-Doe-7000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Jane-Doe-90000'

#how to create new employee from string - split
"""first,last,pay = emp_str1.split("-")
new_emp1 = Employee(first,last,pay)

print(new_emp1.email)"""

#we don't them to parse the string everytime they want to create new employee
# so we will use classmethod- from_string()

"""new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)"""

#Static methods
#take a date and return if it's a workday - logical connection on Employee class but does not depend on any instance or methods
#create a static method in class

import datetime
my_date = datetime.date(2016,7,11)

print(Employee.is_workday(my_date))