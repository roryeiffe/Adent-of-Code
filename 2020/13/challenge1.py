import sys
import math

f = open(sys.argv[1])

earliest = int(f.readline().strip())
buses = f.readline().strip().split(",")

temp = []
for bus in buses:
	if bus.isnumeric():
		temp.append(int(bus))

buses = temp

print(earliest)
print(buses)

# stores list of tuples, first entry is bus id, second entry is earliest departure time
earliest_bus = []

for bus in buses:
	earliest_valid_departure = math.ceil(earliest/bus)
	earliest_bus.append((bus,earliest_valid_departure*bus))

# sort by departure time:
sorted_times = sorted(earliest_bus, key=lambda bus: bus[1]) 

print(sorted_times[0])

answer = (sorted_times[0][1] - earliest) * sorted_times[0][0]
print(answer)
