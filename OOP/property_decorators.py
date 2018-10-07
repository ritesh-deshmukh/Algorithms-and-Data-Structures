class Employee(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.email = first_name + "." + last_name + "@example.com"

    @property
    def email(self):
        return(f"{self.first_name}.{self.last_name}@example.com")

    @property
    def full_name(self):
        return (f"{self.first_name}, {self.last_name}")

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print("Name Deleted")
        self.first_name = None
        self.last_name = None


emp1 = Employee("Jason", "Klum")
# emp2 = Employee("Alex", "Minefield")
emp1.full_name = "Alex Minefield"
# emp1.first_name = "Jim"
print(emp1.first_name)
print(emp1.email)
# print(emp1.last_name)
print(emp1.full_name)

del emp1.full_name