class myClass:
    def __init__(self):
        # private variable inside a class
        self.__privateVar = 10
        self.publicVar = 20

    # privte method inside a class
    def __privateMethod(self, num):
        a = 5 + num
        return "I am a Private method", a

    def publicMethod(self):
        x = self.__privateMethod(4)
        return x

c = myClass()

# print(c.__privateMethod(4))
print(c.publicMethod())
# print(f"Private Var before changing: {c.__privateVar}")
# c._privateVar = 16
# print(f"Private Var after changing: {c.__privateVar}")