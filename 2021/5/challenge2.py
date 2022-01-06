f = open("input.txt")

lines = []
for item in f:
    p1 = item.split('->')[0].split(',')
    p2 = item.split('->')[1].split(',')
    p1 = (int(p1[0]),int(p1[1]))
    p2 = (int(p2[0]),int(p2[1]))
    lines.append((p1,p2))

# find max x and max y:
max_x = 0
max_y = 0
for line in lines:
    p1 = line[0]
    p2 = line[0]
    if p1[0] > max_x:
        max_x = p1[0]
    if p2[0] > max_x:
        max_x = p2[0]
    if p1[1] > max_x:
        max_y = p1[1]
    if p2[1] > max_x:
        max_y = p2[1]

print(max_x)
print(max_y)

grid = []
for i in range(0,max_x+1):
    arr = []
    for j in range(0,max_y+1):
        arr.append(0)
    grid.append(arr)

for line in lines:
    (x1,y1) = line[0]
    (x2,y2) = line[1]

    if y1 == y2:
        low_x = min(x1,x2)
        high_x = max(x1,x2)
        for i in range(low_x,high_x+1):
            grid[y1][i] += 1
    if x1 == x2:
        low_y = min(y1,y2)
        high_y = max(y1,y2)
        for i in range(low_y,high_y+1):
            grid[i][x1] += 1


    


num_twos = 0

for row in grid:
    for item in row:
        if item == 0:
            print('.',end='')
        else:
            print(item,end = "")
            if item > 1:
                num_twos += 1
    print()

print(num_twos)