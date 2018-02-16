import sys
lines = sys.stdin.readlines()


def pad(grd):
    s = [' '*(len(grd[0])+2)]
    grd = [' ' + l.replace('\n', '') + ' ' for l in grd]
    return s + grd + s


def solve(lines):
    grid = pad(lines)
    x = 1
    y = next(i for i, c in enumerate(grid[1]) if c == '|')
    d = 0
    dd = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    out = []
    cnt = 0
    while 1:
        c = grid[x][y]
        if c == ' ': break
        if c == '+':
            f = (d+2)%4

            d = (d if grid[x+dd[d][0]][y+dd[d][1]] != ' ' else
                 next(i for i in range(4) if i != f and
                 grid[x+dd[i][0]][y+dd[i][1]] != ' '))

        if c != '-' and c != '|' and c != '+':
            out.append(c)
        dx, dy = dd[d]
        x, y = x + dx, y + dy
        cnt += 1
    return ''.join(out), cnt


test = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+
""".split('\n')[1:-1]

assert solve(test) == ('ABCDEF', 38)
pt1, pt2 = solve(lines)
print('pt1 {}'.format(pt1))
print('pt2 {}'.format(pt2))
