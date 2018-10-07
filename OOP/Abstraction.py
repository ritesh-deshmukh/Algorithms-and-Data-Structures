from abc import ABCMeta, abstractmethod


# shape is an interface
class Shape:
    # when you use the abstract method,
    # the parent class requires the child class to hava the abstract methods present in the child class
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        return "This is area method inside Shape Parent class"

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(Rectangle, self).__init__()

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)

    # override rectangle area method in Rectangle
    def area(self):
        print("THis is in square overridden method")
        return self.width * self.height

s = Square(5)
print(s.area())
print(s.perimeter())

# rectangle1 = Rectangle(2,5)
# print(f"Area from child Rectangle class: {rectangle1.area()}")
# print(f"Area from child Rectangle class: {rectangle1.perimeter()}")
#
# rectangle2 = Shape()
# print(rectangle2.area())