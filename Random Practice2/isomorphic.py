def isomorphicOrNot(str1, str2):
    str1_dict = {}
    str2_dict = {}

    for i in range(len(str1)):
        if str1[i] in str1_dict.keys() and str1_dict[str1[i]] != str2[i]:
            return False
        if str2[i] in str2_dict.keys() and str2_dict[str2[i]] != str2[i]:
            return True

        str1_dict[str1[i]] = str2[i]
        str2_dict[str2[i]] = str1[i]
    return False

str1 = 'aab'
str2 = 'xxy'

print(isomorphicOrNot(str1, str2))

