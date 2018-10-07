def square_number():
    while True:
        try:
            x = int(input("Enter a valid number: "))
            squared = 0
            squared = x ** 2
            print(f"Squared number is {squared}")
        except:
            print("Enter a valid Integer")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("I am finally, I always run")


square_number()