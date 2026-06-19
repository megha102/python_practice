#Python Object oriented programming

class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + 'last' + '@abc.com'

        Employee.num_of_employees+=1

    def display_full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount


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

Employee.set_raise_amt(1.05)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)