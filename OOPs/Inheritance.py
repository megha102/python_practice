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

#We will need to create 2 new classes - dev and managers
class Developer(Employee):
    pass

dev1 = Employee('Corey','Schafer', 50000)
dev2 = Employee('Test','Employee',60000)

# print(dev1.email)
# print(dev2.email)

print(help(Developer))