import sys

# Given the matrix of seats, as well as i and j coordinates
# return list of the adjacent seats:
def get_adjacent_seats(L,i,j):
	# max possible index of i and j values:
	max_i = len(L) - 1
	max_j = len(L[0]) - 1
	seats = []
	# up left diagonal:
	if i > 0 and j > 0:
		seats.append(L[i-1][j-1])
	# up:
	if i > 0:
		seats.append(L[i-1][j])
	# up right diagonal:
	if i > 0 and j < max_j:
		seats.append((L[i-1][j+1]))
	# right:
	if j < max_j:
		seats.append(L[i][j+1])
	# bottom right diagonal:
	if i < max_i and j < max_j:
		seats.append(L[i+1][j+1])
	# bottom:
	if i < max_i:
		seats.append(L[i+1][j])
	# bottom left diagonal:
	if i < max_i and j > 0:
		seats.append(L[i+1][j-1])
	# left:
	if j > 0:
		seats.append(L[i][j-1])
	return seats

# given list of seats, count how many are occupied:
def count_occupied(adjacent):
	count = 0
	for item in adjacent:
		if item == "#":
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
			if seat == "L" and "#" not in adjacent:
				new_row.append("#")
			elif seat == "#" and count_occupied(adjacent) >= 4:
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
