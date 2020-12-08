import sys
import math

L = []
f = open(sys.argv[1],"r")

for item in f:
	L.append(item.strip())

def find_id(sequence):
	rows = sequence[:7]
	seats = sequence[7:]

	upper = 127
	lower = 0

	for letter in rows:
		half = math.ceil((upper-lower)/2)
		if letter == "F":
			upper -= half
		if letter == "B":
			lower += half

	row = upper

	lower = 0
	upper = 7

	for letter in seats:
		half = math.ceil((upper-lower)/2)
		if letter == "L":
			upper -= half
		if letter == "R":
			lower += half

	seat = lower

	return 8*row+seat

max_id = 0
for sequence in L:
	id = find_id(sequence)
	if id > max_id:
		max_id = id

print(max_id)

