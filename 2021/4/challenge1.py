import numpy as np

def checkBoard(board, numbers):
    # construct a boolean board that incdicates if number was called;
    booleanBoard = []
    for row in board:
        booleanRow = []
        for item in row:
            booleanRow.append(item in numbers)
        booleanBoard.append(booleanRow)
    for row in booleanBoard:
        valid = True
        valid = not (False in row)
        if valid:
            return True
    booleanBoardFlipped = (np.transpose(booleanBoard))
    for col in booleanBoardFlipped:
        valid = True
        valid = not (False in col)
        if valid:
            return True
    
    return False



f = open('input.txt','r')


L = []
for item in f:
    L.append(item)

# get list of called numbers
numbers = L[0].split(',')
temp = []
for item in numbers:
    temp.append(int(item))
numbers = temp.copy()

boards = []
i = 2
while i + 4 < len(L):
    j = 0
    board = []
    while j < 5:
        row = L[i+j].split()
        temp = []
        for item in row:
            temp.append(int(item))
        row = temp.copy()
        board.append(row)
        j += 1
    i += 6
    boards.append(board)

numberSet = set()
for number in numbers:
    found = False
    numberSet.add(number)
    for board in boards:
        if checkBoard(board, numberSet):
            found = True
            break
    if found:
        break

finalNumber = number
            
sum = 0
for row in board:
    for number in row:
        if number not in numberSet:
            sum += number
print(sum * finalNumber)


