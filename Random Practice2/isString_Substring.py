string1 = "neap"
string2 = "pineapple"

if string2.find(string1) is not -1:
    print("Found")
else:
    print("not found")

if string1 in string2:
    print("FOund")
else:
    print("NOt found")
#
#
#
# def isSubstring(string1, string2):
#     len1 = len(string1)
#     len2 = len(string2)
#     i = 0
#     for i in range(0, len2-len1):
#         j = 0
#
#         for j in range(0, len1):
#             if string2[i+j] != string1[j]:
#                 break
#
#         if j == len1:
#             return i
#     return -1
#
# res = isSubstring(string1,string2)
# if res == -1:
#     print("Naah")
# else:
#     print("Yaah {}".format(res))
