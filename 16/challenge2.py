import sys

# given a range string, parse it and return the two numbers:
def parse_range(s):
	result = ""
	for c in s:
		if c.isnumeric() or c == "-":
			result += c
	minval = int(result.split("-")[0])
	maxval = int(result.split("-")[1])
	return minval, maxval

def get_field(s):
	result = ""
	for c in s:
		if c.isnumeric():
			break
		result += c
	result = result.strip()
	return result.strip(":")

class range_set():
	def __init__(self, field,range1,range2):
		self.min1 = range1[0]
		self.max1 = range1[1]
		self.min2 = range2[0]
		self.max2 = range2[1]
		self.field = field
	def __str__(self):
		return self.field
	def valid(self,value):
		return (value >= self.min1 and value <= self.max1) or (value >= self.min2 and value <= self.max2)

L = []
f = open(sys.argv[1])
for item in f:
	L.append(item.strip())

ranges = []
# parse input:
for i in range(len(L)):
	line = L[i]
	if line == "your ticket:":
		my_ticket = L[i+1].split(",")
	elif line == "nearby tickets:":
		others = L[i+1:]
	elif ":" in line:
		split1 = line.split(" or ")
		r = range_set(get_field(split1[0]),parse_range(split1[0]),parse_range(split1[1]))
		ranges.append(r)
# convert my ticket to ints:
for i in range(len(my_ticket)):
	my_ticket[i] = int(my_ticket[i])
# convert others to string
for i in range(len(others)):
	others[i] = others[i].split(",")
# convert others to int:
for i in range(len(others)):
	for j in range(len(others[i])):
		others[i][j] = int(others[i][j])

ticket_error_rate = 0

valid_tickets = []

# loop through tickets:
for ticket in others:
	# loop through fields:
	valid_ticket = True
	for field in ticket:
		# assume field is invalid until we find a range that fits it:
		valid_field = False
		for r in ranges:
			if r.valid(field):
				valid_field = True
		if not valid_field:
			ticket_error_rate += field
			valid_ticket = False
	if valid_ticket:
		valid_tickets.append(ticket)

# number of fields in each ticket:
num_fields = len(valid_tickets[0])

matrix = []
# for each range:
for ticket in valid_tickets:
	L = []
	# for each index:
	for index in range(num_fields):
		# keep track of which ranges are valid for the field
		valid_ranges = []
		for r in ranges:
			if r.valid(ticket[index]):
				valid_ranges.append(r)
		L.append(valid_ranges)
	matrix.append(L)

# Structue of matrix:
# each row is a different ticket
# each column is a different field
# position i,j stores which matrices are valid for that ticket and that position:
# Matrix: 		field 1			field 2			field 3
# ticket 1 		r1, r2 			   r1  				r3
# ticket 2		r1, r2			r2, r3 			r1
# ticket 3 		r2 					r2,r3 				r2

# maps index positiont to which attribute it matches:
position_to_field = dict()
# stores ranges that have already been accounted for:
found_ranges = set()

# loop until we've found every range:
while(len(found_ranges) != len(ranges)):
	# loop through each index:
	for index in range(num_fields):
		# keep track of common ranges between all sets
		common_ranges = set()
		# initialize common_ranges with the first row's ranges:
		for r in matrix[0][index]:
			common_ranges.add(r)
		# go through each ticket in matrix
		for row in matrix:
			current_ranges = set()
			# for each range that corresponds to the current ticket and the current field index:
			for r in row[index]:
				# add range to current ranges:
				current_ranges.add(r)
			# only take ranges that are valid for all sets for this given index
			# in other words, intersect with the cumulative intersection of valid ranges:
			common_ranges = common_ranges.intersection(current_ranges)
		# ignore ranges that we already know that index for:
		common_ranges = common_ranges.difference(found_ranges)
		# if there is only one possible range for this index:
		if len(common_ranges) == 1:
			only_range = common_ranges.pop()
			# add this range to set of found ranges
			found_ranges.add(only_range)
			# update position_to_field dictionary:
			position_to_field[index] = only_range

product = 1
for key in position_to_field:
	if "departure" in position_to_field[key].field:
		product *= my_ticket[key]

print(product)
