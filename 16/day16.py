import sys
lines = sys.stdin.readlines()
ins = lines[0].strip().split(',')
def pt1(ins, sz, line=False):
    if not line:
        line = list(chr(ord('a') + i) for i in range(sz))
    for i in ins:
        if 's' in i:
            d = int(i[1:])
            line = line[-d:] + line[:-d]
        elif 'x' in i:
            a, b = map(int, i[1:].split('/'))
            line[a], line[b] = line[b], line[a]
        else:
            a, b = i[1:].split('/')
            ia = next(j for j, c in enumerate(line) if c == a)
            ib = next(j for j, c in enumerate(line) if c == b)
            line[ia], line[ib] = line[ib], line[ia]

    return ''.join(line)

def pt2(ins, sz, times):
    mp = {}
    l = ''.join(chr(ord('a') + i) for i in range(sz))
    mp[l] = 0
    
    l = pt1(ins, sz, list(l))
    i = 0
    while not l in mp:
        i+=1
        mp[l] = i
        l = pt1(ins, sz, list(l))
    period = i + 1 - mp[l]
    left = times - mp[l]
    last = left%period
    for i in range(last):
        l = pt1(ins, sz, list(l))
    return l

assert pt1(['s1','x3/4','pe/b'], 5) == 'baedc'
print('pt1', pt1(ins, 16))
print('pt2', pt2(ins, 16, 1000000000))

