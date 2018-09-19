# Given a string, find length of the longest substring with all distinct characters.
# For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

word = "abcavnmx"

def longest_distinct(word):
    count = 0
    distinct = []
    word = list(word)
    for i in range(len(word)):
        if word[i] not in distinct:
            distinct += word[i]
        else:
            distinct += " "

    print(distinct)

longest_distinct(word)