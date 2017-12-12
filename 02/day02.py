import sys
lines = sys.stdin.readlines()
def solve():
    c1, c2 = (0, 0)
    for l in lines:
        a = list(map(int, l.split()))
        c1 += max(a) - min(a)
        for x in a:
            for y in a:
                if x != y and x%y == 0:
                    c2 += x//y
    return (c1,c2)
c1, c2 = solve()
print('pt1', c1)
print('pt2', c2)
