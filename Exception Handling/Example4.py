x = 5
y = 0

try:
    print(x/y)
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("For Rest of the exceptions")
finally:
    print("I will always run")
