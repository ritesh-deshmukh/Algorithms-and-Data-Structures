def add():
    while True:
        try:
            result = int(input("Enter a number: "))
        except:
            print("That's not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("End of try/except/finally")

add()