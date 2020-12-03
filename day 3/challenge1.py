import sys
def find_answer(right,down,L):
	numtrees = 0
	i = 0
	j = 0
	while i < len(L):
		line = L[i]
		if line[j] == "#":
			numtrees += 1
		i += down
		j += right
		if j >= len(line):
			j -= len(line)

	
	return numtrees


f = open(sys.argv[1],"r")
L = []
for line in f:
	L.append(line.strip())

inputs = [(1,1),(3,1),(5,1),(7,1),(1,2)]

sum = 1
for t in inputs:
	print(find_answer(t[0],t[1],L))
	sum *= find_answer(t[0],t[1],L)

print(sum)