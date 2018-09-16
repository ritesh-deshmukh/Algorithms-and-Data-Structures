# # Given full name: ("John Smith").
# # Write a function that swaps the first and the last name and inserts a comma in between.
# # if invalid input, print "invalid input"
#
#
name = None

def NameSwap(name):
    if name is not None:
        full_name = name.split(" ")
        if len(full_name) == 2:
            full_name[0], full_name[1] = full_name[1], full_name[0]
            full_name = ", ".join(full_name)
            return full_name
        else:
            return "Invalid input"
    else:
        return "Invalid input"

NameSwap(name)
