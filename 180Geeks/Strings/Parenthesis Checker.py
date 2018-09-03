# Given an expression string exp, examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
# For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

strA = "{([])}"

size = len(strA)

def check_balanced(srtA):
    dict = set([ ('(',')'), ('[',']'), ('{','}') ])
    open = set('([{')

    match = []

    for bracket in srtA:
        if bracket in open:
            match.append(bracket)
        else:
            if len(match) == 0:
                return "Not balanced"
            lastOpen = match.pop()
            if (lastOpen,bracket) not in dict:
                return "Not balanced"

    if len(match) == 0:
        return "Balanced"
print(check_balanced(strA))