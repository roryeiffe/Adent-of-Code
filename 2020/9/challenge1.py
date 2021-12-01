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

answer = -1
preamb = int(sys.argv[2])
i = preamb
while i < len(R):
	sub_list = R[(i-preamb):i]
	if not add_to(sub_list,R[i]):
		answer = R[i]
	i += 1

print(answer)

