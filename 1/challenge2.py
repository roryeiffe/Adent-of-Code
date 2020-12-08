f = open("input.txt","r")
L = []
for line in f:
	L.append(int(line))

for num1 in L:
	for num2 in L:
		for num3 in L:
			if num1 != num2 and num1 != num3 and num1 + num2 + num3 == 2020:
				print(num1,num2,num3,num1*num2*num3)