# Given a string, remove duplicates from it.
# Note that original order of characters must be kept same.
# Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.

word = "aabbccdd"

def remove_duplicates(word):
    word = list(word)
    i = 0
    while i < len(word):
        if word.count(word[i]) > 1:
            del(word[i])
            i += 1
    print(f"Given word without duplicates: {''.join(word)}")

print(f"Given word with duplicates: {word}")
remove_duplicates(word)