from random import *

foo = [1,2,3,4,5,6,7,8,9,0]
random_index = randrange(0,len(foo))
print(foo[random_index])


data = [x for x in range(1000)]

def select_data(data):
    if data != []:
        position = randrange(len(data))
        element = data[position]
        data[position] = data[-1]
        del data[-1]
        return element
    else:
        return None

print(select_data(data))