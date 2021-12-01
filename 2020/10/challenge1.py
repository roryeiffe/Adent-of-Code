import sys
sys.path.insert(1, "../")
import utils

L = utils.parse_file()

R = []
for item in L:
	R.append(int(item))

one_jolt = 0
three_jolt = 0

R.sort()

i = 0
while i < len(R):
	if i == 0:
		difference = R[i] - 0
	else:
		difference = R[i] - R[i-1]
	if difference == 1:
		one_jolt += 1
	elif difference == 3:
		three_jolt += 1
	i += 1

# Need to reach highest adapter with one more three_jolt:
three_jolt += 1

print(one_jolt*three_jolt)