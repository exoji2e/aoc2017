import sys
sys.path.append('..')
from aoclib import *
    
def pt1(inp):
    ins = [int(x) for x in inp.split(',')]
    lst, _, _ = knothash(ins, *start())
    return lst[0]*lst[1]

if __name__ == '__main__':
    assert knot2('') == 'a2582a3a0e66e6e86e3812dcb672a272' 
    assert knot2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    inp = input()
    print('pt1', pt1(inp))
    print('pt2', knot2(inp))
