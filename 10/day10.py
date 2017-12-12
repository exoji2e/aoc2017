l = 256
inp = input()
def knothash(ins, lst, c, u):
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
    
def hx(n):
    return str(n) if n < 10 else chr(ord('a') + n - 10)
def tohex(n):
    return hx(n//16) + hx(n%16)
def start():
    return ([i for i in range(l)], 0, 0)

def pt1():
    ins = [int(x) for x in inp.split(',')]
    lst, c, u = start()
    lst, _, _ = knothash(ins, lst, c, u)
    return lst[0]*lst[1]

def pt2():
    ins = [ord(x) for x in inp] + [17, 31, 73, 47, 23]
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

print('pt1', pt1())
print('pt2', pt2())
