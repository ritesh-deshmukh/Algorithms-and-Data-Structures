# Object oriented programming
# INHERITANCE


class Employee(object):
    def __init__(self, name, age, department):  # constructor function
        self.name = name
        self.age = age
        self.department = department

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.department


class New_Employee(Employee):       # inherit properties of Employee class
    def __init__(self, new_employee_id, name, age, department):  # constructor function, with inherited attributes
        self.new_employee_id = new_employee_id
        super().__init__(name, age, department)      # calling the constructor from Employee function

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.department + " " + str(self.new_employee_id)


emp1 = Employee("Jason", 28, "Engineering")     # Instance of Employee class
print(emp1)

emp2 = New_Employee(44, "Alex", 28, "Engineering")  # Instance of New_Employee class
print(emp2)
