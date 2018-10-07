class Employee(object):

    no_of_emp = 0
    class_variable = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.no_of_emp += 1

    def print_details(self):  # a method
        print(f"Name of Employee: {self.name}")
        print(f"Age of Employee: {self.age}")

    @classmethod
    def change_age(cls, new_age):
        cls.class_variable = new_age

    @staticmethod
    def static_method(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Inherited from Employee
class Developer(Employee):
    class_variable = 25


emp1 = Employee("Jason", 28)
emp2 = Developer("Alex", 34)
emp3 = Developer("Heidi", 20)

# print(isinstance(emp2, Employee))       # check to see if object emp2 is an instance of class Employee => True
# print(isinstance(emp1, Developer))      # check to see if object emp1 is an instance of class Developer => False

print(issubclass(Developer, Employee))      # check to see if Developer is a subclass of Employee
print(issubclass(Employee, Developer))      # check to see if Employee is a subclass of Developer


