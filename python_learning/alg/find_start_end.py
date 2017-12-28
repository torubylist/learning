import re
def find_start_end(s, sub_s):
    result = []
    m      = re.search(sub_s, s)
    gap    = 0
    if m == None:
        return [(-1,-1)]
    while m != None:
        if (m.start() + gap, m.end()-1 + gap) not in result:
            result.append((m.start() + gap, m.end()-1 + gap))
        gap = gap + 1
        m   = re.search(sub_s, s[gap:])

    return result
if __name__ == '__main__':
    s     = str(input())
    sub_s = str(input())

    for x in find_start_end(s,sub_s):
        print(x)
