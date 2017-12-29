# Huge speedup when run with pypy
import sys
lines = sys.stdin.readlines()
sA = int(lines[0].split()[-1].strip())
sB = int(lines[1].split()[-1].strip())
def nxt(seed, fac, l):
    a = (seed*fac)%2147483647
    while not l(a):
        a = (a*fac)%2147483647
    return a


def pt1(A, B, l):
    return solve(A, B, l, lambda x: True, lambda x: True)
def pt2(A, B, l):
    return solve(A, B, l, lambda x: x%4 == 0, lambda x: x%8 == 0)

def solve(A, B, l, l1, l2):
    cnt = 0
    facA, facB = 16807, 48271
    nd = (1<<16) - 1
    for i in range(l):
        A = nxt(A, facA, l1)
        B = nxt(B, facB, l2)
        if (A & nd) == (B & nd):
            cnt += 1
    return cnt

assert pt1(65, 8921, 40000000) == 588
assert pt2(65, 8921, 5000000) == 309
print('pt1 ' + str(pt1(sA, sB, 40000000)))
print('pt2 ' + str(pt2(sA, sB, 5000000)))
