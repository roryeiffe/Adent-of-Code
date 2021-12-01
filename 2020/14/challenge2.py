import sys
# Given a decimal number, convert to binary string
def dec_to_bin(x):
	result = ""
	while True:
		rem = x%2
		result += str(rem)
		x = x//2
		if x == 0:
			break
	return result

def dec_to_bin_helper(x):
	result = dec_to_bin(x)
	return pad_bin(result,36)

# pads a binary number with 0 and returns the reverse:
def pad_bin(x,padding):
	while len(x) < padding:
		x += "0"
	return x

# Given a binary string, convert to decimal:
def bin_to_dec(x):
	result = 0
	x = x[::-1]
	i = 0
	while i < len(x):
		if x[i] == "1":
			result += 2**i
		i += 1
	return result

# Given decimal number, converts to binary, masks it, and returns
# the resulting decimal number
def return_masked_result(mask, x):
	binary = dec_to_bin_helper(x)
	mask = mask[::-1]
	results = []
	num_floating = mask.count("X")
	# Find all possible combinations, given floating point values:
	binary_combinations = return_binary_combination(num_floating)
	# loop through each combination
	for combo in binary_combinations:
		copy = ""
		# i keeps track of which combinatino we are on:
		i = 0
		# j iterates through letters:
		for j in range(len(binary)):
			# if we find an x, replace with the next number in the combination
			if mask[j] == "X":
				# replace letter with current binary number
				copy += combo[i]
				# incrememnt binary combo:
				i += 1
			elif mask[j] == "1":
				copy += "1"
			else:
				copy += binary[j]
		results.append(bin_to_dec(copy[::-1]))
	return results

# Given a number n, return a list of strings where each string is a possible combination os 0's and 1's. 
# ex: return_binary_combination(2) would return ["00","01","10","11"]
def return_binary_combination(n):
	result = []
	i = 0
	while i < 2**n:
		result.append(pad_bin(dec_to_bin(i),n))
		i += 1
	return result

values = dict()

# read input:
f = open(sys.argv[1],"r")
for item in f:
	item = item.strip()
	# whenever there is a new mask, update mask variable:
	if item[0:4] == "mask":
		mask = item.split("=")[1].strip()
	# otherwise, update memory locations:
	elif item[0:3] == "mem":
		# parse input:
		memory_location = ""
		i = 4
		while i < len(item):
			if item[i] == "]":
				break
			memory_location += item[i]
			i += 1
		memory_location = int(memory_location)
		value = int(item.split("=")[1].strip())
		# get all possible addresses:
		addresses = return_masked_result(mask,memory_location)
		# for each address, update dictionary:
		for address in addresses:
			values[address] = value

sum = 0
for key in values:
	sum += values[key]

print(sum)



