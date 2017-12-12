import sys
lines = sys.stdin.readlines()
def modpt1(reg):
    return 1
def modpt2(reg):
    return 1 if reg < 3 else -1

def solve(mod):
    prg = [int(x) for x in lines]
    i, c = (0, 0)
    while i < len(prg):
        nxt = i + prg[i]
        prg[i] += mod(prg[i])
        i = nxt
        c += 1
    return c

print('pt1', solve(modpt1))
print('pt2', solve(modpt2))
