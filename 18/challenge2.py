import sys

# Given an expression with no parentheses, evaluate it using the weird precedence rule:
def parse_expression(e):
	L = e.split("*")
	multiplants = []
	for item in L:
		R = item.split(" ")
		sum = 0
		for number in R:
			if number.isnumeric():
				sum += int(number)
		multiplants.append(sum)
	product = 1
	for item in multiplants:
		product *= item
	return product

def simplify(exp):	
	# nested keeps track of whether we are inside a nested paranethesis expression:
	# ex: ((3 + 4) + 3 * 2) + 34
	#      ^-----^
	#      |     |
	# 3 + 4 is the most nested sub expression in this expression
	nested = False
	# keeps track of the indices of the sub-expressions:
	tuples = []
	first_index = -1
	second_index = -1
	for i in range(len(exp)):
		c = exp[i]
		if not nested:
			# if we found a new parenthesis:
			if c == "(":
				# set nested to be true and update index:
				nested = True
				first_index = i
		# if we're in the process of exploring a nested expression
		if nested:
			# if we find another open parenthesis, we know this isn't 
			# the most nested we can be, so index:
			if c == "(":
				first_index = i
			# if we're closing off this expression, we update the index:
			# and add tuple to our list of tuples:
			elif c == ")":
				nested = False
				second_index = i
				tuples.append((first_index,second_index))

	# next_pair is the next pair we have to look out for:
	# pair counter is which pair we are on:
	pair_counter = 0
	next_pair = tuples[pair_counter]
	new_exp = ""
	# loop through each character in expression
	# append characters that aren't in nested expressions
	# otherwise, append the simplified version of the nested expression:
	i = 0
	while i < len(exp):
		# if we haven't reached the next pair, or we have reached all pairs already:
		if i < next_pair[0] or i > next_pair[1]:
			# just add character by character:
			new_exp += exp[i]
			i += 1
		# otherwise, extract out the sub-expression:
		elif i == next_pair[0]:
			# parse the sub_expression and return the value:
			new_exp += str(parse_expression(exp[next_pair[0]+1:next_pair[1]]))
			# skip to after this expression:
			i = next_pair[1] + 1
			# update which pair we are looking at:
			pair_counter += 1
			# if we haven't run out of pairs, update next_pair
			if pair_counter < len(tuples):
				next_pair = tuples[pair_counter]
	return new_exp

L = []
f = open(sys.argv[1],"r")
for item in f:
	L.append(item.strip())

result = parse_expression("1 + 2 * 3 + 4 * 5 + 6")
print(result)

result = 0
for line in L:
	exp = line

	# while there are no parentheses left in our expression:
	while(exp.count("(") != 0 and exp.count(")") != 0):
		exp = simplify(exp)

	# by the end, we should have one last expression:
	sub_result = parse_expression(exp)
	result += sub_result
	print(sub_result)

print(result)
