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
		return "Values for " + self.field + " must be between " + str(self.min1) + " and " + str(self.max1) + " or between " + str(self.min2) + " and " + str(self.max2)
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

print("answer:",ticket_error_rate)
