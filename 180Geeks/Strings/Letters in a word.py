# Write a generalized function that given 2 words, returns True if the letters in the first word are contained in the second word.

word1 = "test"
word2 = "holiday"

def containsSameLetters(word1,word2):
    count_dict = {}
    temp_arr = [] * len(word1)
    for i in range(len(word2)):
        if word2[i] not in count_dict:
            count_dict[word2[i]] = 1
        else:
            count_dict[word2[i]] += 1

    for i in range(len(word1)):
        if word1[i] in count_dict and count_dict[word1[i]] >= 1:
            temp_arr.append(word1[i])

    if len(temp_arr) == len(word1):
        # print("Found")
        return True
    else:
        # print("Not found")
        return False
    # print(f"Dict: {count_dict}")
    # print(f"Temp arr: {temp_arr}")

containsSameLetters(word1,word2)
