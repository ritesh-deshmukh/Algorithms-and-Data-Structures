lst  = [1,2,3,4]

def rever(lst):
    i = 0
    j = len(lst) - 1

    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    return lst

print(rever(lst))

lst2 = [1,2,3,4]
def rever2(lst):
    l = len(lst)
    for i in range(0, l//2):
        l = l - 1
        hold = lst[i]
        lst[i] = lst[l]
        lst[l] = hold
    return lst

print(f"solution 2: {rever2(lst2)}")