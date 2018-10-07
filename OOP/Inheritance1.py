# Object oriented programming
# INHERITANCE


class Employee(object):

    no_of_emp = 0
    class_variable = 10     # this is a class variable

    def __init__(self, name, age, department):  # constructor function
        self.name = name        # attribute of Employee class
        self.age = age      # attribute of Employee class
        self.department = department        # attribute of Employee class
        Employee.no_of_emp += 1     # increments each time a class instance is made and so number of employees

    def print_details(self):  # a method
        print(f"Name of Employee: {self.name}")
        print(f"Age of Employee: {self.age}")
        print(f"Department of Employee: {self.department}")
        print(f"This is the class variable: {self.class_variable}")


class New_Employee(Employee):       # inherit properties of Employee class
    def __init__(self, new_employee_id, name, age, department):  # constructor function, with attributes inherited from the Employee class
        self.new_employee_id = new_employee_id
        Employee.__init__(self, name, age, department)      # calling the constructor from Employee function

    def print_new_details(self):  # a method
        print(f"New Employee id: {self.new_employee_id}")
        print(self.print_details())


emp1 = Employee("Jason", 28, "Engineering")     # Instance of Employee class, emp1 is an instance variable
# emp1.name, emp1.age, emp1.department = "Alex", 28, "Engineering"
# emp1.name = "Jason"
# emp1.print_details()
# print(f"Number of employees for emp1: {emp1.no_of_emp}")

emp2 = New_Employee(44, "Alex", 28, "Engineering")  # Instance of New_Employee class, emp2 is an instance variable
emp2.print_new_details()  # calling a method from the class Instance defined above
# print(f"Number of employees for emp2: {emp2.no_of_emp}")
# emp3 = New_Employee(44, "Jane", 28, "Engineering")


# print(f"Number of employees for Employee: {Employee.no_of_emp}")