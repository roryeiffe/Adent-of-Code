import sys
sys.path.insert(1, '../')
import utils

def add_to(L,sum):
	for item1 in L:
		for item2 in L:
			if item1 + item2 == sum and item1 != item2:
				return True
	return False

L = utils.parse_file()

R = []
for item in L:
	R.append(int(item))

preamb = int(sys.argv[2])
i = preamb
while i < len(R):
	sub_list = R[(i-preamb):i]
	if not add_to(sub_list,R[i]):
		answer = R[i]
	i += 1

found = False
print(answer)
for i in range(len(R)):
	for j in range(len(R)):
		if sum(R[i:j]) == answer and i != j:
			range_ = R[i:j]
			found = True
			break
	if found == True:
		break

answer2 = max(range_) + min(range_)
print(answer2)

