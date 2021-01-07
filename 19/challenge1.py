import sys

def find(rules, key):
	# base case:
	children = rules[key]
	if isinstance(children[0][0],str):
		f.write(children[0][0])
		return children[0]
	else:
		# each child is a possible path:
		for child in children:
			# each id_ is a rule that has to be on this path:
			if child != children[-1]:
				f.write("(")
			for id_ in child:
				find(rules,id_)
			if child != children[-1]:
				f.write("|")
			else:
				f.write(")")




L = []
f = open(sys.argv[1])
for item in f:
	L.append(item.strip())

rules = dict()
messages = []

is_rule = True
for item in L:
	if item == "":
		is_rule = False
	elif is_rule:
		L = item.split(":")
		rule_id = int(L[0])
		children = L[1].split("|")
		temp1 = []
		for child in children:
			child = child.strip().split(" ")
			temp2 = []
			for child_id in child:
				if child_id.isnumeric():
					temp2.append(int(child_id))
				else:
					temp2.append(child_id.strip('"'))
			temp1.append(temp2)
		rules[rule_id] = temp1
	else:
		messages.append(item)

# write path to output.txt file:
f = open("output.txt","w")
path = find(rules, 0)
f.close()

# read back the path:
f = open("output.txt","r")
path = f.readline()
f.close()

# eliminate trailing parentheses:
path = path.strip("(").strip(")")

path += "\\" + "n"


f = open("output2.txt","w")
f.write("This is the regex expression:\n\n\n")
f.write(path)

f.write("\n\n\nThese are the expressions to match:\n\n\n")
for message in messages:
	f.write(message + "\n")
