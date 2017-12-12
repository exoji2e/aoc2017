def solve(n):
    p1, p2 = (0, 0)
    l = len(n)
    for i in range(l):
        if n[i] == n[i-1]:
            p1 += int(n[i])
        if n[i] == n[i-l//2]:
            p2 += int(n[i])
    return (p1, p2)

n = input()
assert solve("1122")[0] == 3
assert solve("1111")[0] == 4
assert solve("1234")[0] == 0
assert solve("91212129")[0] == 9
assert solve("1212")[1] == 6
assert solve("1221")[1] == 0
assert solve("123425")[1] == 4
assert solve("123123")[1] == 12
assert solve("12131415")[1] == 4

p1, p2 = solve(n)
print('p1:', p1)
print('p2:', p2)
