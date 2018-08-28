# first non repeated character in a given string

str = "geeksforgeeks"

def nonrep(str):
    count_dict = {}

    for char in str:
        count_num = str.count(char)
        count_dict[char] = count_num
        # print(count_num)

    count_dict_sorted = sorted(count_dict.items(), key=lambda x: x[1])

    # for key, value in sorted(count_dict.items(), key=lambda x: x[0]):
    #     print(key,value)


    print(count_dict_sorted)
    print(count_dict_sorted[0][0])
    # print(count_num)

nonrep(str)

