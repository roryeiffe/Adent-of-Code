import sys

f = open(sys.argv[1])

numbers = []

for item in f:
	numbers.append(int(item.strip()))

counter = 0
for i in range(1,len(numbers)):
	if numbers[i] > numbers[i-1]:
		counter += 1

print(counter)