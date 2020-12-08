f = open("input2.txt",'r')
L = []
for item in f:
	L.append(item.strip())

groups = []
# stores key-value pairs (in string form):
group = []
for item in L:
	# if empty line, append passport, and reinitialize passport variable:
	if item == "":
		groups.append(group)
		group = []
	# otherwise, loop through current line and append
	# key value pairs to passport
	if item != "":
		group.append(item)

#get the last one
groups.append(group)

count = 0
for group in groups:
	for letter in group[0]:
		in_all = True
		for person in group:
			if letter not in person:
				in_all = False
		if in_all:
			count += 1


print(count)
