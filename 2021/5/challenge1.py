

def print_grid(grid):
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
    return num_twos

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

grid = []
for i in range(0,max_x+2):
    arr = []
    for j in range(0,max_y+2):
        arr.append(0)
    grid.append(arr)

for line in lines:
    (x1,y1) = line[0]
    (x2,y2) = line[1]

    
    low_x = min(x1,x2)
    high_x = max(x1,x2)
    low_y = min(y1,y2)
    high_y = max(y1,y2)

    # horizontal line
    if y1 == y2:
        for i in range(low_x,high_x+1):
            grid[y1][i] += 1
    # vertical line
    if x1 == x2:
        for i in range(low_y,high_y+1):
            grid[i][x1] += 1
    # diagonal line
    if (y1 != y2) and (x1 != x2):
        print((x1,y1),'->',(x2,y2))
        xPositions = []
        yPositions = []
        if x2 > x1:
            xPositions = list(range(x1,x2+1))
        elif x1 > x2:
            xPositions = list(range(x2,x1+1))
            xPositions.reverse()
            
        if y2 > y1:
            yPositions = list(range(y1,y2+1))
        elif y1 > y2:
            yPositions = list(range(y2,y1+1))
            yPositions.reverse()
        
        print(xPositions)
        print(yPositions)
        
        for i in range(len(xPositions)):
            grid[yPositions[i]][xPositions[i]] += 1
    



    



answer = print_grid(grid)
print(answer)
