def index(s, sub):
    start = 0
    end = 0
    while start < len(s):
        if s[start+end] != sub[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub):
            return s[start],start
    return -1

print(index("hihellopubsa","hello"))