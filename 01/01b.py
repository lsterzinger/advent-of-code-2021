import numpy as np

depths = np.loadtxt('input01.txt')

current_window = 0
old_window = sum(depths[0:3])

counter = 0

for i in range(1, len(depths)-2):
    current_window = sum(depths[i:i+3])
    if current_window > old_window:
        counter += 1
    old_window = current_window

counter 


