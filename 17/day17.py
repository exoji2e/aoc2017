import sys
lines = sys.stdin.readlines()
inp = int(lines[0])
def pt1(sz):
    l = [0]
    c = 0
    for i in range(1, 2018):
        c = (c + sz)%i
        l = l[:c+1] + [i] + l[c+1:]
        c += 1
    return l[(c+1)%len(l)]

def pt2(sz):
    last = 0
    c = 0
    for i in range(1, 50000000):
        c = (c + sz)%i
        if c == 0:
            last = i
        c += 1
    return last

assert pt1(3) == 638
print('pt1', pt1(301))
print('pt2', pt2(301))
