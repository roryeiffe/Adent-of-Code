f = open("input.txt","r")

numvalid = 0

for line in f:
	L = line.split(" ")
	range_ = L[0].split("-")
	lower = int(range_[0])
	upper = int(range_[1])
	letter = L[1].strip(":")
	password = L[2]
	count = 0
	for c in password:
		if c == letter:
			count += 1
	if count >= lower and count <= upper:
		numvalid += 1
print(numvalid)