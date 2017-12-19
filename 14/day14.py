from collections import *
import sys
sys.path.append("..")
from aoclib import *

def bitc(i):
    return bin(i).count('1')

def bitv(c):
    if ord('0') <= ord(c) <= ord('9'):
        return int(c)
    else:
        return ord(c) - ord('a') + 10

def solve(s):
    z = 128
    pt1 = 0
    grd = [[0]*z for _ in range(z)]
    d = [[0]*z for _ in range(z)]
    for r in range(z):
        hsh = knot2(s + '-' + str(r))
        pt1 += sum(bitc(bitv(d)) for d in hsh)
        for i, h in enumerate(hsh):
            s2 = list(reversed(bin(bitv(h))))[:-2]
            for j, v in enumerate(s2):
                grd[r][(i+1)*4 - 1 - j] = v == '1'
    c = 0
    for i in range(z):
        for j in range(z):
            if not (d[i][j] == 0 and grd[i][j]): continue
            c += 1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if not (0 <= x < z and 0 <= y < z): continue
                if grd[x][y] and d[x][y] == 0:
                    d[x][y] = c
                    q.append((x+1, y))
                    q.append((x-1, y))
                    q.append((x, y-1))
                    q.append((x, y+1))
    return pt1, c
            
assert solve('flqrgnkx') == (8108, 1242)
pt1, pt2 = solve('nbysizxe')
print('pt1', pt1)
print('pt2', pt2)
