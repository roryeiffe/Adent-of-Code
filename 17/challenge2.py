import sys

# Given L, adds a column based on the <where>
# parameter, either at the begginning or end
def add_col(grids,where):
	for L in grids:
		for row in L:
			if where == "end":
				row.append(".")
			elif where == "begin":
				row.insert(0,".")

	return grids

def add_row(grids,where):
	for L in grids:
		new_row = []
		for i in range(len(L[0])):
			new_row.append(".")
		if where == "end":
			L.append(new_row)
		elif where == "begin":
			L.insert(0,new_row)
	return grids

def add_grid(grids,where):
	new_grid = []
	for i in range(len(grids[0])):
		new_row = []
		for j in range(len(grids[0][0])):
			new_row.append(".")
		new_grid.append(new_row)
	if where == "end":
		grids.append(new_grid)
	elif where == "begin":
		grids.insert(0,new_grid)
	return grids

def add_dimensions(grids):
	grids = add_col(grids, "end")
	grids = add_col(grids, "begin")
	grids = add_grid(grids, "end")
	grids = add_grid(grids,"begin")
	grids = add_row(grids, "end")
	grids = add_row(grids, "begin")
	return grids

def print_grids(grids):
	for grid in grids:
		for row in grid:
			for item in row:
				print(item,end = "")
			print()
		print()

# returns a list of tuples which represent the offsets
# that we look for neighbors:
def get_combos():
	result = []
	ranges = [0,-1,1]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				if not (ranges[i] == 0 and ranges[j] == 0 and ranges[k] == 0):
					result.append((ranges[i],ranges[j],ranges[k]))
	return result


L = []
f = open(sys.argv[1],"r")
for item in f:
	item = item.strip()
	R = []
	for c in item:
		R.append(c)
	L.append(R)

grids = [L]

# add an extra layer on each dimension:
grids = add_dimensions(grids)

print("Before")
print_grids(grids)

combos = get_combos()

cycles = 0
while cycles < 6:
	new_grids = []
	for i in range(0,len(grids)):
		grid = []
		for j in range(0,len(grids[0])):
			row = []
			for k in range(0,len(grids[0][0])):
				neighbors = []
				for combo in combos:
					i_ = i + combo[0]
					j_ = j + combo[1]
					k_ = k + combo[2]
					# if neighbor is of bounds (exceeds max):
					if (i_ >= len(grids)) or (j_ >= len(grids[i])) or (k_ >= len(grids[i][j])):
						neighbors.append(".")
					# if neighbor exceeds minimum bounds:
					elif (i_ < 0) or (j_ < 0) or (k_ < 0):
						neighbors.append(".")
					else:
						neighbors.append(grids[i_][j_][k_])
				# if active
				if grids[i][j][k] == "#":
					# if 2 or 3 neighbors stay active, otherwise become inactive:
					if not (neighbors.count("#") == 3 or neighbors.count("#") == 2):
						row.append(".")
					else:
						row.append("#")
				# if inactive:
				elif grids[i][j][k] == ".":
					# if 3 active neighbors, become active, otherwise remain inactive:
					if neighbors.count("#") == 3:
						row.append("#")
					else:
						row.append(".")
			# append row to grid
			grid.append(row)
		# append grid to grids:
		new_grids.append(grid)

	grids = new_grids.copy()
	# add new dimension each time:
	grids = add_dimensions(grids)
	cycles += 1


# count how many active 
num_active = 0
for grid in grids:
	for row in grid:
		for item in row:
			if item == "#":
				num_active += 1
print(num_active)
