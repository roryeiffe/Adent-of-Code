import sys

# recursive search through bag dictionary:
def search(bag_contains, current):
	children = bag_contains[get_bag(current)]
	# base cases
	# if this bag does not contain any other bags:

	# each level is how many bags are in this current bag (including children)
	# base case: since there are no children, we are just counting how many bags
	# are in our current bag, and no children
	if len(children) == 0:
		print(current)
		return int(get_num(current))
	
	recursion = []
	for child in children:
		grandchildren = bag_contains[get_bag(child)]
		if len(grandchildren) == 0:
			recursion.append(int(get_num(child)))
		else:
			recursion.append(search(bag_contains,child))

	print(get_bag(current), "has", recursion, "inner bags")

	# make sure we count this current bag:
	return int(get_num(current)) + int(get_num(current))*sum(recursion)

# given a bag string, return only the name of the bag:
# ex: 1 light blue returns light blue
def get_bag(bag_string):
	return bag_string.split(" ")[1] + " " + bag_string.split(" ")[2]

# given a bag string, return the quantity:
# ex: 1 light blue returns 1
def get_num(bag_string):
	return bag_string.split(" ")[0]

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
			current_bag = rule_list[i-3] + " " + rule_list[i-2] + " " + rule_list[i-1]
			# this means no bags
			if get_bag(current_bag) != "no other":
				bag_contains[this_bag].append(current_bag)
		i += 1

print(search(bag_contains,"2 dark green"))
print(search(bag_contains,"1 shiny gold"))

	

