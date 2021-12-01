import sys

def parse_instruction(word):
	L = word.split(" ")
	cmd = L[0]
	arith = L[1][0]
	num = int(L[1][1:])
	return cmd,arith,num

f = open(sys.argv[1])
L = []
for item in f:
	L.append(item.strip("\n"))

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
		break

print(accumlator)
