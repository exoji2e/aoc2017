from collections import *
n = int(input())
def solve():
    c = Counter()
    x, y, r, d = (0, 0, 0, 0)
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    c[(x, y)] = 1
    pt2 = None
    for i in range(n-1):
        if r == x == y:
            r, x, d = (r+1, x+1, 0)
        else:
            x, y = (x + dx[d], y + dy[d])
        if r == abs(x) == abs(y): d+=1
        s = sum(c[(x+i, y+j)]
                for i in [-1, 0, 1]
                for j in [-1, 0, 1])
        c[(x,y)] = s
        if pt2 == None and s > n:
            pt2 = s
    return (abs(x) + abs(y), pt2)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
