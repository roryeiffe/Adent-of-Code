import sys
import math
# Given a direction, returns cardinal direction that is 90
# degrees to the right
def get_right(direction):
	if direction == "east":
		return "south"
	if direction == "south":
		return "west"
	if direction == "west":
		return "north"
	if direction == "north":
		return "east"

# Given a direction, returns cardinal direction that is 90 degrees to the left
def get_left(direction):
	if direction == "east":
		return "north"
	if direction == "north":
		return "west"
	if direction == "west":
		return "south"
	if direction == "south":
		return "east"


f = open(sys.argv[1],"r")

L = []

for item in f:
	direction = item.strip()[0]
	value = int(item.strip()[1:])
	L.append((direction,value))

north_south = 0
east_west = 0
ship_direction = "east"

for item in L:
	direction = item[0]
	value = item[1]

	if direction == "R":
		turns = int(value/90)
		for i in range(turns):
			ship_direction = get_right(ship_direction)
	elif direction == "L":
		turns = int(value/90)
		for i in range(turns):
			ship_direction = get_left(ship_direction)
	elif direction == "N" or (ship_direction == "north" and direction == "F"):
		north_south += value
	elif direction == "S" or (ship_direction == "south" and direction == "F"):
		north_south -= value
	elif direction == "E" or (ship_direction == "east" and direction == "F"):
		east_west += value
	elif direction == "W" or (ship_direction == "west" and direction == "F"):
		east_west -= value

answer = abs(north_south) + abs(east_west)
print(answer)

	