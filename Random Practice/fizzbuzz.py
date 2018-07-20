# arr = [a for a in range(1,21)]
# arr2 = [] * len(arr)
# print(arr)

for num in range(1,21):
    if num%3 == 0 and num%5 == 0:
        # arr2.append("FizzBuzz")
        print("FizzBuzz", end=" ")
    elif num%3 == 0:
        # arr2.append("Fizz")
        print("Fizz", end=" ")
    elif num%5 == 0:
        # arr2.append("Buzz")
        print("Buzz", end=" ")
    else:
        # arr2.append(num)
        print(num, end=" ")

# print(arr2)

# Encapsulation
# polymorphism
# garbage collector
# linkedlist
# hashtable

