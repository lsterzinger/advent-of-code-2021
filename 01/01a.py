import numpy as np

depths = np.loadtxt('input.txt')

counter = 0

for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        counter +=1 

print(counter)
