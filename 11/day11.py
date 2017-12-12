ins = input().split(',')
def dist(x, y):
    return abs(x) + max(abs(y) - abs(x), 0)//2
def solve():
    x, y, d = (0, 0, 0)
    for i in ins:
        if len(i) == 2:
            x += ('w' in i)*2 - 1
            y += ('s' in i)*2 - 1
        else:
            y += (i == 's')*4 - 2
        d = max(d, dist(x, y))
    return (dist(x, y), d)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
