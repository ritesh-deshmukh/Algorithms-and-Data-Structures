# Given two strings, check whether two given strings are anagram of each other or not.
# An anagram of a string is another string that contains same characters, only the order of characters can be different.
# For example, “act” and “tac” are anagram of each other.


word1 = 'geeksforgeeks'
word2 = 'forgeeksgeeks'

def anagram(word1, word2):
    word_dict = {}
    char_found_count = 0
    char_notfound_count = 0

    for i in range(len(word1)):
        if word1[i] not in word_dict:
            word_dict[word1[i]] = word1.count(word1[i])

    for char in word2:
        if char in word_dict:
            char_found_count += 1
        else:
            char_notfound_count += 1

    if char_notfound_count == 0:
        return "Found"
    else:
        return "Not found"

print(f"Given Words: '{word1}' and '{word2}'")
print(f"Anagram result: {anagram(word1,word2)}")