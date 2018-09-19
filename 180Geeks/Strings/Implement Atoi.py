# Your task  is to implement the function atoi.
# The function takes a string(str) as argument and converts it to an integer and returns it.

word = "123a"

def check_number(char):
    return char.isdigit()

def atoi(word):
    num = []
    for i in range(len(word)):
        if check_number(word[i]):
            num.append(word[i])
            print(word[i])
        else:
            print(f"Not a number: {word[i]}")
    print(f"Number in string: {''.join(num)}")

print(f"Given string: {word}")
atoi(word)

