import sys

# Given seats L and cordinates i and j, construct a list of 
# booleans of whether or not the person can see any occupied seats
def get_adjacent_seats(L,original_i,original_j):
	seats = []
	increments = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
	
	for increment in increments:
		i = original_i
		j = original_j
		while(True):
			found = False
			i += increment[0]
			j += increment[1]
			if i < 0 or j < 0:
				break
			try:
				# if we've found an empty seat:
				if L[i][j] == "L":
					break
				# if we've found an occupied seat:
				elif L[i][j] == "#":
					found = True
					break
			# If we've reached the edge of the list, that means we haven't found an occupied seat
			except IndexError:
				break
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
