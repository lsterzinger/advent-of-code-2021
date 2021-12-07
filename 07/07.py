import numpy as np

def parse(input):
    return [int(a) for a in input.split(',')]


def find_cheapest(crabs, constant = True):

    min = np.inf
    imin = 0
    for i in range(max(crabs)+1):
        d = 0
        for c in crabs:
            diff = abs(c-i)
            if constant:
                d += diff
            else:
                d += int((diff * (diff+1))/2)
        if d < min:
            min = d
            imin = i
    return min, imin


sample = """16,1,2,0,4,2,7,1,2,14"""

with open('input07.txt') as inf:
    crabs = inf.read()

assert find_cheapest(parse(sample)) == (37,2)
assert find_cheapest(parse(sample), constant=False) == (168,5)

p1min, p1index = find_cheapest(parse(crabs))
p2min, p2index = find_cheapest(parse(crabs), constant=False)
print(f"Part 1: Minimum fuel of {p1min} at index {p1index}")
print(f"Part 2: Minimum fuel of {p2min} at index {p2index}")
