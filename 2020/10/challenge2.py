import sys
sys.path.insert(1, "../")
import utils
count = 0

# counts the number of distinct paths from source to dest in nodes:
def count_paths_helper(nodes, source, dest):
	global count
	count = 0
	visited = [source]
	count_paths(nodes, visited, dest)
	answer = count
	count = 0
	return answer

# using a visited list, keeps track of how many distinct paths there are
# using the global variable "count"
def count_paths(nodes, visited, dest):
	global count
	# take children of most recently visited child:
	children = nodes[visited[-1]]
	for node in children:
		# if we've already traversed this node:
		if node in visited:
			continue
		# if we've reached the destination:
		if node == dest:
			visited.append(node)
			count += 1
			visited.pop()
			break
	for node in children:
		if node in visited or node == dest:
			continue
		visited.append(node)
		count_paths(nodes,visited,dest)
		visited.pop()

L = utils.parse_file()

R = set()
for item in L:
	R.add(int(item))

R.add(0)
R.add(max(R)+3)

nodes = dict()

i = 0
for node in R:
	nodes[node] = []
	if node + 1 in R:
		nodes[node].append(node+1)
	if node + 2 in R:
		nodes[node].append(node+2)
	if node + 3 in R:
		nodes[node].append(node+3)

#Take it piece by piece. Find how many paths there are from 0 to the first node that has no childen. Then multiply that by each consecutive "chunk"
# populate necessary nodes with nodes that every path will traverse:
neccessary_nodes = [0]
for node in nodes:
	if len(nodes[node]) == 1:
		neccessary_nodes.append(nodes[node][0])

answer = 1
i = 1
while i < len(neccessary_nodes) - 1:
	answer *= count_paths_helper(nodes, neccessary_nodes[i-1],neccessary_nodes[i])
	i += 1

print(answer)


#Take it piece by piece. Find how many paths there are from 0 to the first node that has no childen. Then multiplt that by each consecutive "chunk"
