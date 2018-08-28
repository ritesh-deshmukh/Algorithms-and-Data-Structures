# find if a string has the given word

str1 = 'asd'
str = list(str1)
str2 = ['s','a','d']
n = len(str)
left = 0
right = n-1

def anagram(str, str2, left, right):
    if left == right:
        if str == str2:
            print("found", str)
        else:
            print("Not found", str2, str)
    else:
        for i in range(left, right+1):
            str[left], str[i] = str[i], str[left]
            anagram(str, str2, left+1, right)
            str[left], str[i] = str[i], str[left]


anagram(str, str2, 0, n-1)