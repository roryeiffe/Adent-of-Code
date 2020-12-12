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

# position of the ship:
north_south = 0
east_west = 0
# position of the waypoint, relative to the ship:
waypoint_north_south = 1
waypoint_east_west = 10

ship_direction = "east"
for item in L:
	direction = item[0]
	value = item[1]

	# 90 to the right is the same as 270 to the left:
	if (direction == "R" and value == 90) or (direction == "L" and value == 270):
		temp = waypoint_east_west
		waypoint_east_west = waypoint_north_south
		waypoint_north_south = -temp
	# 180 is the same, no matter which direction:
	elif (direction == "R" or direction == "L") and value == 180:
		waypoint_east_west = -waypoint_east_west
		waypoint_north_south = -waypoint_north_south
	# 270 to the right same as 90 to left:
	elif (direction == "R" and value == 270) or (direction == "L" and value == 90):
			temp = waypoint_north_south
			waypoint_north_south = waypoint_east_west
			waypoint_east_west = -temp

	# Move the waypoint:
	elif direction == "N":
		waypoint_north_south += value
	elif direction == "S":
		waypoint_north_south -= value
	elif direction == "E":
		waypoint_east_west += value
	elif direction == "W":
		waypoint_east_west -= value

	# move to waypoint by <value> number of times:
	elif direction == "F":
		north_south += value*waypoint_north_south
		east_west += value*waypoint_east_west

answer = abs(north_south) + abs(east_west)
print(answer)

	