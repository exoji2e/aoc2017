from math import ceil
def solve():
    l = list(map(int, input().split()))
    n = len(l)
    s = {str(l): 0}
    c = 1
    while 1:
        m = max(l)
        i = next(i for i, v in enumerate(l) if v == m)
        add = ceil(m/n)
        l[i] = 0
        for j in range(1, n+1):
            l[(i+j)%n] += min(m, add)
            m -= min(m, add)
        k = str(l)
        if k in s: return (c, c - s[k])
        else: s[k] = c
        c+=1

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
