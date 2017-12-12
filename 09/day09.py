import re
from functools import reduce
def f(a, c):
    return (a[0], a[1] + 1) if c == '{' else (sum(a), a[1] - 1)

def solve():
    s = input()
    s = re.sub(r'!.', '', s)
    l = len(s)
    s = re.sub(r'<[^>]+>', '<>', s)
    pt2 = l - len(s)
    s = re.sub(r'[^{}]', '', s)
    tot, _ = reduce(f, s, (0, 0))
    return (tot, pt2)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
