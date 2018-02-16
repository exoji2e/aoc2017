from collections import Counter, deque
import sys
lines = sys.stdin.readlines()


def extract(l, vals):
    a = l.strip().split()
    if len(a) == 2:
        return getv(a[1], vals)
    return a[1], getv(a[2], vals)


def getv(s, vals):
    try:
        return int(s)
    except:
        return vals[s]


def ev(i, msgs, vals, ins, lines):
    last = -1
    out = deque()
    ch = False
    ret = None
    x = {'i': i}
    while x['i'] < len(lines):
        l = lines[x['i']]
        if 'snd' not in l and 'rcv' not in l:
            s, v = extract(l, vals)
        exec(ins[l[:3]])
        x['i'] += 1
        if ret is not None:
            return ret
        ch = True


def pt1(ls):
    ins = {'set': 'vals[s]=v', 'add': 'vals[s]+=v',
           'mul': 'vals[s]*=v', 'mod': 'vals[s]%=v',
           'snd': 'last=extract(l, vals)', 
           'rcv': 'if extract(l, vals)!=0: ret = last',
           'jgz': 'if vals[s] > 0: x["i"]+=v-1'}
    return ev(0, None, Counter(), ins, ls)


def pt2(lines):
    i, j = 0, 0
    ins = {'set': 'vals[s]=v', 'add': 'vals[s]+=v',
           'mul': 'vals[s]*=v', 'mod': 'vals[s]%=v',
           'snd': 'out.append(extract(l, vals))',
           'rcv': """v = l.strip().split()[1]
if not msgs: ret = x["i"], out, ch
else: vals[v] = msgs.popleft()""",
           'jgz': 'if getv(s, vals) > 0: x["i"]+=v-1'}
    cnt = 0
    vals0 = Counter()
    vals1 = Counter()
    vals1['p'] = 1
    msg0 = deque()
    msg1 = deque()
    ch = True
    while ch:
        i, msg0, ch = ev(i, msg1, vals0, ins, lines)
        cnt += len(msg0)
        j, msg1, ch = ev(j, msg0, vals1, ins, lines)
    return cnt


test = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".split('\n')

assert pt1(test) == 4
print('pt1 {}'.format(pt1(lines)))
assert pt2(test) == 1
print('pt2 {}'.format(pt2(lines)))
