def reverse_name(nam):
    name = list(nam)
    left = 0
    right = len(name) - 1

    while left < right:
        name[left], name[right] = name[right], name[left]
        left += 1
        right -= 1

    return name

def pal(name):
    if list(name) == reverse_name(name):
        print("yes", list(name), reverse_name(name))
    else:
        print("No")

# iterative
def isPal(name):
    for i in range(0, len(name)//2):
        if name[i] != name[len(name) - i - 1]:
            return False
        return True
print(f"Ispal = {isPal('malayalam')}")
pal("malayal")