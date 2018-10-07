# special methods are always surrounded by double __ <== 2 underscores (dunder)


class Employee(object):

    def __init__(self, name, age):      # dunder init methood called whenever class is called and sets the attributes provided
        self.name = name
        self.age = age

    # def print_details(self):  # a method
    #     print(f"Name of Employee: {self.name}")
    #     print(f"Age of Employee: {self.age}")

    # unambiguous representation of an object used for debugging and logging
    def __repr__(self):
        return (f"FROM __repr__ => Name: {self.name}, Age: {self.age}")

    # readable representation of an object used for display for end user
    def __str__(self):
        return (f"FROM __str__ = > Name: {self.name}, Age: {self.age}")

    def __add__(self, other):
        return self.age + other.age

    def __len__(self):
        return len(self.name)


emp1 = Employee("Jasons", 28)
emp2 = Employee("Janet", 20)
# print(emp1)
print(repr(emp1))       # called emp1.__repr__()
print(str(emp1))        # called emp1.__str__()

print(int.__add__(1,2))     # add method for int
print(str.__add__('a','b'))     # add method for str


print(f"Add dunder method: {emp1 + emp2}")


print(len(emp1))