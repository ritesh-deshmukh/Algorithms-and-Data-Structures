def f(s):
    if s == "":
        return [""]
    result = []
    for p in f(s[1:]):
        for i in range(len(p) + 1):
            # p_i = s[0] + p[i:]
            # p_i = p[:i-1] + s[i] + p[i+1:]
            # p_i = p[:i] + s[0] + p[i:]
            p_i = p[:i] + s[0]
            result.append(p_i)

    return result



if __name__ == '__main__':
    print (len(f('abcde')))