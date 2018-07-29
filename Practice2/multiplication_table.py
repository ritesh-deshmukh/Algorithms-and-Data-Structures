num1 = int(input("Enter the table number: "))
num2 = int(input("Enter the table limit number: "))
print("Multiplication Tables")

# Table number whos table is to be displayed
for j in range(num1, num1+1):
    print("\n")
    print(j, '|')

    if num2 > 0:
        # how many iterations of that table
        for k in range(1, num2 + 1):
            print('\t', j, ' * ', k, '= ', j * k)
    else:
        print("Please enter a valid number")


print("\n")