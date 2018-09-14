# Write a code function segment that prints out all the numbers from 1-100
# print 'fizz' if that number is divisible by 3, and 'buzz' if that number is divisible by 8.

nums = [i for i in range(1,101)]

for num in nums:
    if num % 24 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 8 == 0:
        print("Buzz")
    else:
        print(num)


