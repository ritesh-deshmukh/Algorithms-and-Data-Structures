name = 'hiseasytext'


def count_char(name, char):
    num = 0

    for i in range(len(name)):
        if name[i] == char:
            return i        # first occurrence
            num += 1
    # return num


print(count_char(name, 't'))
