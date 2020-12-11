import sys

def return_count(number):
	L = []
	for item in range(number):
		L.append(item+1)


	count = 0
	for i in range(len(L)):
		for j in range(len(L) + 1):
			if j > i:
				count += len(L[i:j])
	return count

for i in range(100):
	count = return_count(i)
	print(i,count)