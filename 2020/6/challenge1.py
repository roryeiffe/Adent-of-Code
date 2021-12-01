f = open("input2.txt",'r')
L = []
for item in f:
	L.append(item.strip())

groups = []
# stores key-value pairs (in string form):
group = ""
for item in L:
	# if empty line, append passport, and reinitialize passport variable:
	if item == "":
		groups.append(group)
		group = ""
	# otherwise, loop through current line and append
	# key value pairs to passport
	group += item

#get the last one
groups.append(group)

count = 0
for group in groups:
	distinct_letters = set()
	for letter in group:
		distinct_letters.add(letter)
	count += len(distinct_letters)
print(count)
