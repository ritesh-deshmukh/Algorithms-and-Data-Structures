'''
Error prone code
def add(n1, n2):
    return n1+n2


number1 = 10
number2 = input("Enter a number: ")

print(add(number1, number2))
'''


def add(n1, n2):
    try:
        return n1 + n2
    except:
        x = n1 + int(n2)
        print(f"Answer: {x}")
        return
    finally:
        print("I will always print")
        return


number1 = 10
number2 = input("Enter a number: ")

add(number1, number2)

