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
	while len(result) < 36:
		result += "0"
	return result[::-1]

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
	binary = dec_to_bin(x)[::-1]
	mask = mask[::-1]
	result = ""
	i = 0
	while i < len(binary):
		if mask[i] == "0":
			result += "0"
		elif mask[i] == "1":
			result += "1"
		else:
			result += binary[i]
		i += 1
	return bin_to_dec(result[::-1])

values = dict()

f = open(sys.argv[1],"r")
for item in f:
	item = item.strip()
	if item[0:4] == "mask":
		mask = item.split("=")[1].strip()
	elif item[0:3] == "mem":
		memory_location = ""
		i = 4
		while i < len(item):
			if item[i] == "]":
				break
			memory_location += item[i]
			i += 1
		memory_location = int(memory_location)
		value = int(item.split("=")[1].strip())
		values[memory_location] = return_masked_result(mask,value)

sum = 0
for key in values:
	sum += values[key]

print(sum)


