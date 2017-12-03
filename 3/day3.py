from collections import *
n = int(input())
def solve():
    c = Counter()
    x, y, r = (0, 0, 0)
    c[(x, y)] = 1
    pt2 = None
    for i in range(n-1):
        if r == x == y:
            r += 1
            x += 1
        elif x == r != -y:  y -= 1
        elif -y == r != -x: x -= 1
        elif -x == r != y:  y += 1
        else:               x += 1
        s = sum(c[(x+dx, y+dy)] 
                for dx in [-1, 0, 1] 
                for dy in [-1, 0, 1])
        c[(x,y)] = s
        if pt2 == None and s > n:
            pt2 = s
    return (abs(x) + abs(y), pt2)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
