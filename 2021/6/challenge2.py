import math

x = 256

coeff = 5.5149
factor = .0872

answer = coeff * (math.e**(factor*x))import sys
import math

f = open(sys.argv[1], "r")
fishes = f.readline().split(",")
for i in range(len(fishes)):
    fishes[i] = int(fishes[i])
f.close()
f = open("output.csv", "w")

dayToFish = dict()

for day in range(150):
    f.write(str(day))
    f.write(',')
    f.write(str(len(fishes)))
    f.write('\n')
    dayToFish[day] = len(fishes)
    for i in range(len(fishes)):
        fish = fishes[i]
        if fish != 0:
            fishes[i] -= 1
        else:
            fishes[i] = 6
            fishes.append(8)

# prevNumFishes = 1
# for day in dayToFish:
#     numFishes = dayToFish[day]
#     print(day, " ", numFishes / prevNumFishes)
#     prevNumFishes = numFishes
