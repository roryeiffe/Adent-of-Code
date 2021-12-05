import util
import sys

file = open(sys.argv[1], 'r')

horizontal = 0
vertical = 0
aim = 0

for item in file:
    L = item.split()
    direction = L[0]
    value = int(L[1])
    if direction == 'forward':
        horizontal += value
        vertical += aim*value
    elif direction == 'up':
        aim -= value
    elif direction == 'down':
        aim += value

print(horizontal*vertical)
