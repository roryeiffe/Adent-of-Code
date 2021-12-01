import sys

def parse_instruction(word):
	L = word.split(" ")
	cmd = L[0]
	arith = L[1][0]
	num = int(L[1][1:])
	return cmd,arith,num

def try_instructions(L):
	non_broken = True
	visited_indices = set()
	i = 0
	accumlator = 0
	while i < len(L):
		visited_indices.add(i)
		instruction = L[i]
		cmd, arith, num = parse_instruction(instruction)
		if cmd == "acc":
			if arith == "+":
				accumlator += num
			else:
				accumlator -= num
			i += 1
		elif cmd == "jmp":
			if arith == "+":
				i += num
			else:
				i -= num
		else:
			i += 1
		if i in visited_indices:
			non_broken = False
			break
	return non_broken, accumlator


f = open(sys.argv[1])
L = []
for item in f:
	L.append(item.strip("\n"))

for i in range(len(L)):
	cmd,arith,num = parse_instruction(L[i])
	new_string = L[i]
	if cmd == "nop":
		new_string = "jmp" + " " + arith + str(num)
	elif cmd == "jmp":
		new_string = "nop" + " " + arith + str(num)
	R = L.copy()
	R[i] = new_string
	non_broken,accumlator = try_instructions(R)
	if non_broken:
		print(accumlator)
	i += 1

