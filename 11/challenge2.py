import sys

# Given seats L and cordinates i and j, construct a list of 
# booleans of whether or not the person can see any occupied seats
def get_adjacent_seats(L,original_i,original_j):
	max_i = len(L) - 1
	max_j = len(L[0]) - 1
	seats = []
	# up left diagonal:
	found,i,j = False, original_i, original_j
	while (i > 0 and j > 0):
		if L[i-1][j-1] == "L":
			break
		if L[i-1][j-1] == "#":
			found = True
		i,j = i-1,j-1
	seats.append(found)

	# up:
	found,i,j = False, original_i, original_j
	while (i > 0):
		if L[i-1][j] == "L":
			break
		if L[i-1][j] == "#":
			found = True
		i -= 1
	seats.append(found)

	# up right diagonal:
	found,i,j = False, original_i, original_j
	while (i > 0 and j < max_j):
		if L[i-1][j+1] == "L":
			break
		if L[i-1][j+1] == "#":
			found = True
		i,j = i-1,j+1
	seats.append(found)

	# right:
	found,i,j = False, original_i, original_j
	while (j < max_j):
		if L[i][j+1] == "L":
			break
		if L[i][j+1] == "#":
			found = True
		j += 1
	seats.append(found)

	# bottom right diagonal:
	found,i,j = False, original_i, original_j
	while (i < max_i and j < max_j):
		if L[i+1][j+1] == "L":
			break
		if L[i+1][j+1] == "#":
			found = True
		i,j = i+1, j+1
	seats.append(found)

	# bottom:
	found,i,j = False, original_i, original_j
	while(i < max_i):
		if L[i+1][j] == "L":
			break
		if L[i+1][j] == "#":
			found = True
		i += 1
	seats.append(found)

	# bottom left diagonal:
	found,i,j = False, original_i, original_j
	while(i < max_i and j > 0):
		if L[i+1][j-1] == "L":
			break
		if L[i+1][j-1] == "#":
			found = True
		i,j = i+1,j-1
	seats.append(found)

	# left:
	found,i,j = False, original_i, original_j
	while (j > 0):
		if L[i][j-1] == "L":
			break
		if L[i][j-1] == "#":
			found = True
		j -= 1
	seats.append(found)

	return seats

# given list of seats, count how many are occupied:
def count_occupied(adjacent):
	count = 0
	for item in adjacent:
		if item == True:
			count += 1
	return count

def apply_rules(seats):
	new_seats = []
	for i in range(len(seats)):
		new_row = []
		for j in range(len(seats[i])):
			seat = seats[i][j]
			adjacent = get_adjacent_seats(seats,i,j)
			# if empty seat and no occupied seats around, becomes occupied:
			if seat == "L" and True not in adjacent:
				new_row.append("#")
			elif seat == "#" and count_occupied(adjacent) >= 5:
				new_row.append("L")
			else:
				new_row.append(seats[i][j])
		new_seats.append(new_row)
	return new_seats

def print_seats(L):
	for row in L:
		for seat in row:
			print(seat,end="")
		print()


f = open(sys.argv[1],"r")
seats = []
for item in f:
	row = []
	for letter in item.strip():
		row.append(letter)
	seats.append(row)

while(True):
	new_seats = apply_rules(seats)
	if new_seats == seats:
		break
	seats = new_seats

occupied = 0
for row in seats:
	for seat in row:
		if seat == "#":
			occupied += 1

print(occupied)
