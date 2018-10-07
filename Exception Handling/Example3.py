'''
for i in ['a','b', 'c']:
    print(i**2)
'''

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)

except:
    print("This will never work")

finally:
    print("The code should be: \n --------------------------\n"
          "for i in [1, 2, 3]:\n"
          "\t print(i ** 2)\n"
          "for output:\n1\n4\n9")