# http://code.activestate.com/recipes/496807-list-of-all-combination-from-multiple-lists/

# a = [[1,2,3], [4,5,6]]
# r=[[]]
# for x in a:
#     t = []
#     for y in x:
#         for i in r:
#             t.append(i+[y])
#     r = t
#
# print(len(r))
# for x in r:
#     print(x)

# output = 1,2,3 => 14,24,34 => 15,25,35 => 16,26,36 => 147,247,347 => 157,257,357 ...

# simplified version
# a = [[1,2,3], [4,5,6], [7,8,9]]
# r=[[]]
# for x in a:
#     t = []
#     r = [ i + [y] for y in x for i in r ]
#
# print(len(r))
# for x in r:
#     print(x)





def comb(data):
    if len(data) <= 1:
        return [data]
    res = []
    for i, c in enumerate(data):
        for r in comb(data[:i]+data[i+1:]):
            res.append([c]+r)
    return res

data = [1,2,3,4]
print(comb(data))




def combinations(n, list, combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos

print(combinations(3,"abcd"))

# import itertools
# print(list(itertools.permutations([1,2,3])))





# string1 = [['a','b'], ['c', 'd', 'e'], ['f', 'g']]
# n = len(string1)
#
# def permute(string1, l, r):
#     if l == r:
#         print(string1)
#     else:
#         for i in range(l,r+1):
#             string1[l], string1[i] = string1[i], string1[l]
#             permute(string1, l+1, r)
#             string1[l], string1[i] = string1[i], string1[l]
#
# permute(string1, 0, n-1)