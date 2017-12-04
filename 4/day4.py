import sys
lines = sys.stdin.readlines()
def solve():
    c1, c2 = (0,0)
    for l in lines:
        s1, s2 = (set(), set())
        split = l.split()
        for s in split:
            s1.add(s)
            s2.add(str(sorted(s)))
        if len(split) == len(s1):
            c1+=1
        if len(split) == len(s2):
            c2+=1
    return (c1, c2)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
