import sys

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

"""

N % 7 == 0
N % 13 == 1
N % 59 == 4
N % 31 == 6
N % 19 == 7

N % 7 == 0
(N - 1) % 13 == 0
(N - 4) % 59 == 0
(N - 6) % 31 == 0
(N - 7) % 19 == 0


(N - index) % id = [N%id - index%id] % id
(a - b) % n = [a%n - b%n] % n
"""