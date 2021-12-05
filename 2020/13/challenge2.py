import sys
import math
import time

class bus:
	# initializes a bus with an id number and index number:
	def __init__(self,id,index):
		self.id = id
		self.index = index

	def __str__(self):
		return "I am a bus with id " + str(self.id) + " and index " + str(self.index) + "."

	# returns true if bus can leave at time
	# false otherwise
	def isValid(self,time):
		if time % self.id == 0:
			return True
		else:
			return False

# given a number, returns 
def find_prime_factors(n):
	L = []
	# first, check how many twos are in n:
	while n % 2 == 0:
		L.append(2)
		n = n/2

	# check other factors:
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i == 0:
			L.append(int(i))
			n = n/i

	# if n is a prime number:
	if n > 2:
		L.append(int(n))

	return L


# given list of numbers, finds lowest common multiple:
def find_lcm(L):
	# first construct a list of all factors in any number:
	factors = set()
	for item in L:
		for factor in find_prime_factors(item):
			factors.add(factor)
	answer = 1
	# now , for each factor, find the greatest number of times it appears in any number:
	for factor in factors:
		max_appearances = 0
		for item in L:
			# check count of current factor in prime factos of current number
			count = find_prime_factors(item).count(factor)
			if count > max_appearances:
				max_appearances = count
		answer *= (factor**max_appearances)
	return answer


f = open(sys.argv[1])
earliest_time = int(f.readline().strip())
buses = f.readline().strip().split(",")
temp = []

i = 0
for id in buses:
	if id.isnumeric():
		temp.append(bus(int(id),i))
	i += 1

buses = temp

for bus in buses:
	print("((N mod {}) + {}) mod {} == 0".format(bus.id, bus.index % bus.id, bus.id))
# We need to find a number N such that, for each bus in buses:
# N + buses.index is divisible by buses.id
# N + buses.index % buses.id == 0
def find_N(buses):
	

answer = 0 
while(True):
	answer += 1
	cond = True
	for bus in buses:
		if ((answer % bus.id) + (bus.index % bus.id)) % bus.id != 0:
			cond = False
	if cond:
		break


print("Final:",answer)

#3417

# (i + bus.index) mod bus.id = ((i mod bus.id) + (bus.index mod bus.id)) mod bus.id