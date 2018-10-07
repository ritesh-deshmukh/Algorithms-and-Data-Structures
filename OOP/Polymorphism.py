class Animal_1:
    def sound(self):
        print("Sound from Animal_1")

# this class also has the sound method that behaves differently
class Animal_2:
    def sound(self):
        print("Sound from Animal_2")

def make_sound(animal_type):
    return animal_type.sound()


animal1 = Animal_1()
animal2 = Animal_2()

# using the objects of classes to make the classes behave in a different way
make_sound(animal1)
make_sound(animal2)