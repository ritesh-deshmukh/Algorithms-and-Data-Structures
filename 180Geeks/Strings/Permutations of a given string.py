# Given a string, print all permutations of a given string.


string = list('ABC')

def permutations(string, step = 0):
    if step == len(string):
        print ("".join(string), end=" ")
    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)

print(f"Given string: {string}")
print("Permuatations:")
permutations(string)
