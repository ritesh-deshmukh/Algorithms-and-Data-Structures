set1 = ['a', 'b', 'c']
text1 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']

set2 = [1, 2, 3]
text2 = [] * len(text1)


for char in text1:
    for letter in range(len(set1)):
        if char == set1[letter]:
            text2.append(set2[letter])

print(text2)



# set1 = ['a', 'b', 'c']
# text1 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c']
#
# set2 = [1, 2, 3]
# text2 = [] * len(text1)
# # text2 = [1, 1, 1, 2, 2, 2, 3, 3]
#
# for char in text1:
#     for n in range(len(set1)):
#         if char == set1[n]:
#             text2.append(set2[n])
#
#
# print(text2, end="")