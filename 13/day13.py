import sys
lines = sys.stdin.readlines()
blocks = {}
for l in lines:
    l = l.strip()
    a, b = map(int,l.split(': '))
    blocks[a] = b

sz = max(blocks.items())[0]
def cnt(dt):
    s = 0
    for x, v in blocks.items():
        if (x + dt) % ((v - 1)*2) == 0:
            s += x*v
    return s

def pt1():
    return cnt(0)

def pt2():
    dt = 0
    jmp = 720720
    valid = [True for _ in range(jmp)]
    for x, v in blocks.items():
        ran = (v-1)*2
        if jmp%ran == 0:
            fail = (-x)%ran
            for i in range(0, jmp, ran):
                valid[i+fail] = False
    steps = [i for i, v in enumerate(valid) if v]
    dt = 0
    finish = 0
    while not finish:
        for s in steps:
            if cnt(dt+s) == 0:
                return dt + s
        dt += jmp

print('pt1', pt1())
print('pt2', pt2())
