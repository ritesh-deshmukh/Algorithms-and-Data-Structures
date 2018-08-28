# reverse workds in a string

text = "this is a problem"

def rev(text):
    text_split = text.split(" ")
    # print(text_split)
    lst = []
    count = 1
    for _ in range(len(text_split)):
        lst.append(text_split[len(text_split) - count])
        count += 1
    # print(lst)

    # output = text_split[::-1]
    # print(output)

rev(text)



new_text1 = "this is a problem"
new_text = new_text1.split(" ")

def reve(text):
    if len(text) == 0:
        return

    temp = text[0]
    reve(text[1:])
    print(temp, end=" ")

reve(new_text)