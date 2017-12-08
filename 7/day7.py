from collections import *
import sys
lines = sys.stdin.readlines()
lines = [l.strip() for l in lines]
def dfs(i, adj, w):
    sz = w[i]
    k = -1
    subs = []
    s = Counter()
    for d in adj[i]:
        k, f = dfs(d, adj, w)
        if f != -1:
            return (k, f)
        subs.append((d, k))
        s[k] += 1
    if len(s) < 2:
        return (sz + len(adj[i])*k, -1)
    # assumes node that fails has at least 2 siblings.
    kfail = next(k for k, v in s.items() if v == 1)
    kcorr = next(k for k, v in s.items() if v != 1)
    idi = next(i for i, k in subs if k == kfail)
    return (kcorr - kfail + w[idi], idi)
            
def solve():
    mp = {}
    revmp = {}
    n = len(lines)
    w = [0]*n
    w2 = [0]*n
    for i, l in enumerate(lines):
        ll = l.split()
        a = ll[0]
        mp[a] = i
        revmp[i] = a
        w[i] = int(ll[1][1:-1])
    adj = [[] for _ in range(n)]
    parents = [0]*n
    for l in lines:
        try:
            a, b = l.split(' -> ')
        except:
            continue
        i = mp[a.split()[0]]
        for x in b.split(', '):
            parents[mp[x]] +=1
            adj[i].append(mp[x])
    for i, d in enumerate(parents):
        if d == 0:
            v, _ = dfs(i, adj, w)
            return (revmp[i], v)

pt1, pt2 = solve()
print('pt1', pt1)
print('pt2', pt2)
