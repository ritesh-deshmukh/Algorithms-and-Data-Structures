class Greeter:
    def __init__(self, boss):

        self.last = None
        self.print_called = False
        if boss:

            self.boss = boss
            self.boss_enters = True

    def enters(self, visitor):
        # self.print_called = True
        if self.boss_enters:
            self.boss_enters = False

        self.last = visitor

    def greet(self):
        if self.boss_enters:
             return "Hello, {}".format(self.boss)
        else:
            return "Welcome, {}".format(self.last)
        self.print_called = True

g = Greeter("Chuck")
g.enters('John')
print(g.greet())
print(g.greet())

