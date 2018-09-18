# Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
# Input : X = "abcdxyz", y = "xyzabcd"
# Output : 4
# The longest common substring is "abcd" and is of
# length 4.

word1 = "abcdxyz"
word2 = "xyzabcd"

def longest_common_substring(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    result = ""

    for i in range(word1_len):
        match = ""
        for j in range(word2_len):
            if (i+j) < word1_len and word1[i+j] == word2[j]:
                match += word2[j]
            else:
                if len(match) > len(result):
                    result = match
                match = ""
    return result

print(longest_common_substring(word1, word2))