import sys
f = open(sys.argv[1],"r")
# holds the starting numbers
starting = []
for item in f:
	starting.append(int(item.strip()))

# keys are numbers, value is list of turns on which the value was said:
numbers = dict()

# start on turn 1:
turn = 1
# for each starting number, initialize empty list for turns which number was said on:
# and add the current turn:
for number in starting:
	numbers[number] = []
	numbers[number].append(turn)
	turn += 1

# the most recent number was the last starting number
prev_number = starting[-1]
while turn <= 2020:
	# if the previous number was said for the first time, the new number is the difference,
	# that means it appears in at least 2 turns (length greater than 1)
	if len(numbers[prev_number]) > 1:
		# difference in turns:
		new_number = numbers[prev_number][-1] - numbers[prev_number][-2]
	# otherwise, if this is the first time the number was said:
	else:
		new_number = 0
	# update the numbers dictionary:
	if new_number not in numbers:
		numbers[new_number] = [turn]
	else:
		numbers[new_number].append(turn)
	# update turn counter and prev_number
	turn += 1
	prev_number = new_number
	

print(new_number)


