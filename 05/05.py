import numpy as np

sample = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
def parse_input(input):
    lines = input.split('\n')
    lines = [l.split(' -> ') for l in lines]

    inst = []
    for l in lines:
        try:
            x1, y1 = [int(a) for a in l[0].split(',')]
            x2, y2 = [int(a) for a in l[1].split(',')]
            inst.append([x1, y1, x2, y2])
        except ValueError:
            break
    return np.asarray(inst)

def build_grid(lines):
    x = np.concatenate((lines[:,0], lines[:,2]))
    y = np.concatenate((lines[:,1], lines[:,3]))
    
    xmax, ymax = x.max() + 1, y.max() + 1
    
    # print(f"Building grid {xmax} x {ymax}")
    return np.zeros((ymax, xmax))

def analyse(lines, diag=False):
    grid = build_grid(lines)
    for l in lines:
        x1 , y1, x2, y2 = l

        # row
        if y1 == y2:
            # Order min/max
            x1a, x2a = min(x1, x2), max(x1, x2)
            grid[y1, x1a:x2a+1] += 1

        # column
        elif x1 == x2:
            # Order as min/max
            y1a, y2a = min(y1, y2), max(y1,y2)
            grid[y1a:y2a+1, x1] += 1
        
        # diagonal
        else:
            if diag:
                grid = diagonal(grid, (x1, y1, x2, y2))
                continue
            else:
                continue

    return np.unique(grid,return_counts=True)[1][2:].sum()

def diagonal(grid, limits):
    x1, y1, x2, y2 = limits

    dx = int(x2 - x1)
    sx = int(dx/abs(dx))
    dy = int(y2 - y1)
    sy = int(dy/abs(dy))
    m = int(dy/dx)

    for x, y in zip(range(  x1, x2 + sx, sx), range(y1, y2 + sy, sy)):
        #     print('\t', x, y)
            grid[y,x] +=1
    return grid

assert analyse(parse_input(sample)) == 5
assert analyse(parse_input(sample), diag=True) == 12

with open('./input05.txt') as inf:
    lines = parse_input(inf.read())

ans1 = analyse(lines)
ans2 = analyse(lines, diag=True)
print(f"Part 1: {ans1}\nPart 2: {ans2}")
