import sys

# Given L, adds a column based on the <where>
# parameter, either at the begginning or end
def add_col(cubes,where):
	for cube in cubes:
		for grid in cube:
			for row in grid:
				if where == "end":
					row.append(".")
				elif where == "begin":
					row.insert(0,".")
	return cubes

def add_row(cubes,where):
	for cube in cubes:
		for grid in cube:
			new_row = []
			for i in range(len(grid[0])):
				new_row.append(".")
			if where == "end":
				grid.append(new_row)
			elif where == "begin":
				grid.insert(0,new_row)
	return cubes

def add_grid(cubes,where):
	for cube in cubes:
		new_grid = []
		for i in range(len(cube[0])):
			new_row = []
			for j in range(len(cube[0][0])):
				new_row.append(".")
			new_grid.append(new_row)
		if where == "end":
			cube.append(new_grid)
		elif where == "begin":
			cube.insert(0,new_grid)
	return cubes

def add_cube(cubes, where):
	new_cube = []
	for i in range(len(cubes[0])):
		new_grid = []
		for j in range(len(cubes[0][0])):
			new_row = []
			for k in range(len(cubes[0][0][0])):
				new_row.append(".")
			new_grid.append(new_row)
		new_cube.append(new_grid)

	if where == "end":
		cubes.append(new_cube)
	elif where == "begin":
		cubes.insert(0,new_cube)
	return cubes


def add_dimensions(cubes):
	cubes = add_col(cubes, "end")
	cubes = add_col(cubes, "begin")
	cubes = add_grid(cubes, "end")
	cubes = add_grid(cubes,"begin")
	cubes = add_row(cubes, "end")
	cubes = add_row(cubes, "begin")
	cubes = add_cube(cubes, "end")
	cubes = add_cube(cubes, "begin")
	return cubes

def print_cubes(cubes):
	for cube in cubes:
		for grid in cube:
			for row in grid:
				for item in row:
					print(item,end = "")
				print()
			print()
		print("\n")

# returns a list of tuples which represent the offsets
# that we look for neighbors:
def get_combos():
	result = []
	ranges = [0,-1,1]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				for l in range(3):
					if not (ranges[i] == 0 and ranges[j] == 0 and ranges[k] == 0 and ranges[l] == 0):
						result.append((ranges[i],ranges[j],ranges[k],ranges[l]))
	return result


L = []
f = open(sys.argv[1],"r")
for item in f:
	item = item.strip()
	R = []
	for c in item:
		R.append(c)
	L.append(R)

cubes = [[L]]

# add an extra layer on each dimension:
cubes = add_dimensions(cubes)

combos = get_combos()

cycles = 0
while cycles < 6:
	new_cubes = []
	for h in range(0,len(cubes)):
		cube = []
		for i in range(0,len(cubes[0])):
			grid = []
			for j in range(0,len(cubes[0][0])):
				row = []
				for k in range(0,len(cubes[0][0][0])):
					neighbors = []
					for combo in combos:
						h_ = h + combo[0]
						i_ = i + combo[1]
						j_ = j + combo[2]
						k_ = k + combo[3]
						# if neighbor is of bounds (exceeds max):
						if (h_ >= len(cubes)) or (i_ >= len(cubes[h])) or (j_ >= len(cubes[h][i])) or (k_ >= len(cubes[h][i][j])):
							neighbors.append(".")
						# if neighbor exceeds minimum bounds:
						elif (h_ < 0) or (i_ < 0) or (j_ < 0) or (k_ < 0):
							neighbors.append(".")
						else:
							neighbors.append(cubes[h_][i_][j_][k_])
					# if active
					if cubes[h][i][j][k] == "#":
						# if 2 or 3 neighbors stay active, otherwise become inactive:
						if not (neighbors.count("#") == 3 or neighbors.count("#") == 2):
							row.append(".")
						else:
							row.append("#")
					# if inactive:
					elif cubes[h][i][j][k] == ".":
						# if 3 active neighbors, become active, otherwise remain inactive:
						if neighbors.count("#") == 3:
							row.append("#")
						else:
							row.append(".")
				# append row to grid
				grid.append(row)
			# append grid to grids:
			cube.append(grid)
		new_cubes.append(cube)

	cubes = new_cubes.copy()
	# add new dimension each time:
	cubes = add_dimensions(cubes)
	cycles += 1


# count how many active 
num_active = 0
for cube in cubes:
	for grid in cube:
		for row in grid:
			for item in row:
				if item == "#":
					num_active += 1
print(num_active)
