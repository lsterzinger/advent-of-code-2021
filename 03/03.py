import numpy as np 

# Import report
report = np.loadtxt("input03.txt", dtype=str)

# Get number of lines and number of bits per line
nlines = len(report)
nbits = len(report[0])

# Function to find the most (or least) common bit in a given position
def find_most_common(report, b, least_common=False):
    n0 = 0
    n1 = 0

    for line in report:
        if line[b] == '0':
            n0 += 1
        else:
            n1 += 1

    if n0 == n1:
        return 'eq'
    elif n0 > n1:
        if least_common:
            return '1'
        else:
            return '0'
    else:
        if least_common:
            return '0'
        else:
            return '1'


# Return only lines with given valid bit
def pull_valid(l, b, v):
    valid = []
    for line in l:
        if line[b] == v:
            valid.append(line)

    return valid

# Initialize empty arrays
gamma = ['0' for i in range(nbits)]
epsilon = ['0' for i in range(nbits)]

oxy = report
co2 = report

# Loop over bit locations
for b in range(nbits):
    
    common = find_most_common(report, b)
    if common == '1':
        gamma[b] = '1'
    else:
        epsilon[b] = '1'

    oxy_bit = find_most_common(oxy, b)
    oxy_bit = '1' if oxy_bit == 'eq' else oxy_bit

    co2_bit = find_most_common(co2, b, least_common=True)
    co2_bit = '0' if co2_bit == 'eq' else co2_bit

    valid_oxy = pull_valid(oxy, b, oxy_bit)
    valid_co2 = pull_valid(co2, b, co2_bit)

    oxy = valid_oxy
    co2 = valid_co2

    if len(oxy) == 1:
        oxyf = int("".join(a for a in oxy), 2)
    if len(co2) == 1:
        co2f = int("".join(a for a in co2), 2)
    

gamma = int(''.join(a for a in gamma), 2)
epsilon = int(''.join(a for a in epsilon), 2)



print("Part 1: ",gamma * epsilon)
print("Part 2: ", co2f * oxyf)
