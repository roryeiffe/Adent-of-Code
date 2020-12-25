import sys

def find(rules, key, path):
	# base case:
	children = rules[key]
	if isinstance(children[0][0],str):
		print(children[0][0],end="")
		return children[0]
	else:
		# each child is a possible path:
		for child in children:
			possible_path = []
			# each id_ is a rule that has to be on this path:
			print("(",end="")
			for id_ in child:
				possible_path.append(find(rules,id_,path))
			print(")",end="")
			path.append(possible_path)
		path.append(".")
		return path




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

print("Rules:")
for key in rules:
	print(key,":",rules[key])
print("\nMessages:")
for message in messages:
	print(message)

path = find(rules, 0,[])

print("\nPaths:")
for step in path:
	print(step)
# Possible combinations:
# aaaabb
# aaabab
# abbabb
# abbbab
# aabaab
# aabbbb
# abaaab
# ababbb