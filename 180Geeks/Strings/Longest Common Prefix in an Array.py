# Given a array of N strings, find the longest common prefix among all strings present in the array.

group_words = ["apple", "ape", "april"]


def longest_common_prefix(group_words):
    if not group_words:
        return ""

    for i in range(len(group_words[0])):
        for string in group_words[1:]:
            if i >= len(string) or string[i] != group_words[0][i]:
                return group_words[0][:i]
    return group_words[0]

# print(f"Given words: {word for word in group_words}")
for word in group_words:
    print(f"Given words: {word}")
print(f"The longest common prefix is: {longest_common_prefix(group_words)}")