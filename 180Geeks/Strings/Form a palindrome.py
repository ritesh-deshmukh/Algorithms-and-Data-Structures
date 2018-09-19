# Given a string, find the minimum number of characters to be inserted to convert it to palindrome.

word = "ab"

def check_palindrome(str, start, end):
    while (start < end):

        if (str[start] != str[end]):
            return False
        start += 1
        end - -1
    return True

def findMinInsert(word, len_word):
    for i in range(len_word - 1, -1, -1):
        if check_palindrome(word, 0, i):
            return len_word - i - 1, word[len_word - i - 1]


print(findMinInsert(word, len(word)))