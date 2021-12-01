import sys

f = open(sys.argv[1])

numbers = []

for item in f:
	numbers.append(int(item.strip()))

counter = 0
for i in range(2,len(numbers)-1):
	sum1 = numbers[i] + numbers[i-1] + numbers[i-2]
	sum2 = sum1 - numbers[i-2] + numbers[i+1]
	if sum2 > sum1:
		counter += 1

print(counter)