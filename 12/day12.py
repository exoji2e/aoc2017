from collections import *
import sys
lines = sys.stdin.readlines()
def solve():
    adj = [[] for _ in lines]
    for i, l in enumerate(lines):
        l = l.strip().split('<-> ')[1]
        for x in l.split(', '):
            adj[i].append(int(x))
    c = 0
    s = set()
    for i in range(len(adj)):
        if i in s: continue
        s.add(i)
        q = deque([i])
        while q:
            now = q.popleft()
            for nxt in adj[now]:
                if not nxt in s:
                    s.add(nxt)
                    q.append(nxt)
        if i == 0:
            pt1 = len(s)
        c += 1
    return (pt1, c)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
