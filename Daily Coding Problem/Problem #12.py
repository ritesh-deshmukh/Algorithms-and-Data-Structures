# input = 'aaaaaabbbbbccccddddeeeedddddd'
#
# def removeDuplicate(input):
#     temp = set()
#     answer = []
#     for char in input:
#         if char not in temp:
#             answer.append(char)
#             temp.add(char)
#     result = ''.join(answer)
#     return result
#
# print(removeDuplicate(input))

# input = 'aaaaaabbbbbccccddddeeeedddddd'
# answer = []
# for char in input:
#     if char not in answer:
#         answer.append(char)
# answer = ''.join(answer)
# print(answer)


def removeDuplicate(input):
    answer = []
    for char in input:
        if char not in answer:
            answer.append(char)
    answer = ''.join(answer)
    return answer


input = 'aaaaaabbbbbccccddddeeeedddddd'
print(f"String before removing duplicates: {input}")
print(f"String after removing duplicates: {removeDuplicate(input)}")