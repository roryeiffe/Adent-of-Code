f = open("input.txt","r")

numvalid = 0

for line in f:
	L = line.split(" ")
	range_ = L[0].split("-")
	lower = int(range_[0])
	upper = int(range_[1])
	letter = L[1].strip(":")
	password = L[2]

	first = password[lower-1]
	second = password[upper-1]
	if (first == letter and second != letter) or (second == letter and first != letter):
		numvalid += 1
	
print(numvalid)