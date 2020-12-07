import sys

def search(bag_contains, current, end):
	children = bag_contains[current]
	# base cases
	if end in children:
		return 1
	elif len(children) == 0:
		return 0
	else:
		recursion = []
		for bag in children:
			recursion.append(search(bag_contains,bag,end))
		return max(recursion)


f = open(sys.argv[1],"r")
L = []
for item in f:
	L.append(item.strip())

# dictionary where key is bag and values are which bags can be stored:
bag_contains = dict()

for rule in L:
	rule_list = rule.split(" ")
	# this bag is always going to be the first 2 words:
	this_bag = rule_list[0] + " " + rule_list[1]
	# insert into dictionary:
	if this_bag not in bag_contains:
		bag_contains[this_bag] = []
	i = 3
	# loop through rest of list:
	while i < len(rule_list):
		word = rule_list[i].strip(",").strip(".")
		# if we find a bag, grab the last 2 words (these will be the color)
		if (word == "bag" or word == "bags"):
			current_bag = rule_list[i-2] + " " + rule_list[i-1]
			# this means no bags
			if current_bag != "no other":
				bag_contains[this_bag].append(current_bag)
		i += 1


counter = 0
for bag in bag_contains:
	counter += search(bag_contains,bag,"shiny gold")

print(counter)
	
