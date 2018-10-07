class Employee(object):

    no_of_emp = 0
    class_variable = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.no_of_emp += 1

    # regular method below - this method receives the instance as the first argument
    def print_details(self):  # a method
        print(f"Name of Employee: {self.name}")
        print(f"Age of Employee: {self.age}")

    # class method below - the method receives the class as the first argument instead of the instance
    @classmethod
    def change_age(cls, new_age):
        cls.class_variable = new_age

    # static method below - this method does not take anything as the first argument
    @staticmethod
    def static_method(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Jason", 28)
# print(emp1.class_variable)
emp2 = Employee("Alex", 34)
# print(emp2.class_variable)

# Employee.change_age(5)      # same as Employee.class_variable = 5
#
# print(Employee.class_variable)
# print(emp1.class_variable)
# print(emp2.class_variable)

import datetime
my_day = datetime.date(2018, 7, 8)

print(Employee.static_method(my_day))