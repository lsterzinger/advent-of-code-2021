import numpy as np
import pandas as pd

class Sub:
    def __init__(self):
        self.x = 0
        self.z1 = 0
        self.z2 = 0
        self.aim = 0

    def move(self, row):
        direction = row['dir']
        dist = row['dist']
        if direction == 'forward':
            self.x += dist
            self.z2 += (self.aim * dist)

        if direction == 'up':
            self.z1 -= dist
            self.aim -= dist

        if direction == 'down':
            self.z1 += dist
            self.aim += dist


course = pd.read_csv('input02.txt', sep=' ', names=('dir', 'dist'))
sub = Sub()

for i, row in course.iterrows():
    sub.move(row)

print("Part 1: ", sub.x * sub.z1)
print("Part 2: ", sub.x * sub.z2)



