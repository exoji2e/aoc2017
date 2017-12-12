from collections import *
import sys
lines = sys.stdin.readlines()
def solve():
    c = Counter()
    m2 = 0
    for l in lines:
        l = l.strip()
        v, o, val, _, c1, o2, c2 = l.split()
        if eval(str(c[c1]) + o2 + c2):
            if o == 'inc': c[v] += int(val)
            else: c[v] -= int(val)
            m2 = max(m2, c[v])
    m = max(c.items(), key=lambda x: x[1])[1]
    return (m, m2)
pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
