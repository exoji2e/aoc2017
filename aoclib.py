import hashlib
def md5(s):
    return hashlib.md5(s.encode()).hexdigest()
# xxx: k1:v1, k2:v2, ... kn:vn
def kwdict(s):
    d = {}
    sp = s.split(':')
    fst = sp[0]
    s = ':'.join(sp[1:])
    for kv in s.split(','):
        k, v = kv.split(':')
        d[k.strip()] = v.strip()
    return (fst, d)

def hx(n):
    return str(n) if n < 10 else chr(ord('a') + n - 10)
def tohex(n):
    return hx(n//16) + hx(n%16)

def knothash(ins, lst, c, u):
    l = 256
    for i in ins:
        s = c
        e = (c + i) % l
        c = (c + u + i)%l
        u += 1
        if i == 0: continue
        if s < e:
            rev = lst[s:e]
            lst = lst[:s] + rev[::-1] + lst[e:]
        else:
            rev1, rev2 = (lst[s:], lst[:e])
            l2 = len(rev1)
            rev = (rev1 + rev2)[::-1]
            
            lst = rev[l2:] + lst[e:s] + rev[:l2]
    return (lst, c, u)

def start():
    return ([i for i in range(256)], 0, 0)

def knot2(s):
    ins = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    lst, c, u = start()
    for _ in range(64):
        lst, c, u = knothash(ins, lst, c, u)
    out = []
    for i in range(16):
        a = 0
        for j in range(16):
            a ^= lst[i*16 + j]
        out.append(tohex(a))
    return ''.join(out)

