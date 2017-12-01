def p1(n):
    s = 0
    l = len(n)
    for i in range(l):
        if n[i] == n[(i+1)%l]:
            s += int(n[i])
    return s

def p2(n):
    s = 0
    l = len(n)
    for i in range(l):
        if n[i] == n[(i+l//2)%l]:
            s += int(n[i])
    return s

n = input()
assert p1("1122") == 3
assert p1("1111") == 4
assert p1("1234") == 0
assert p1("91212129") == 9
assert p2("1212") == 6
assert p2("1221") == 0
assert p2("123425") == 4
assert p2("123123") == 12
assert p2("12131415") == 4

print('p1:', p1(n))
print('p2:', p2(n))
