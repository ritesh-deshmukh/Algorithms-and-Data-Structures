# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

def autocomplete(qstring, s):
    # print(qstring)
    # print(s)

    check_string = s
    for string in qstring:
        if check_string in string:
            print(string)


qstring = ["dog", "deer", "deal"]
s = "de"

autocomplete(qstring,s)