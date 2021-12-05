import sys

def convertFromBinary(string):
    string = string[::-1]
    answer = 0
    for i in range(0,len(string)):
        digit = int(string[i])
        if digit == 1:
            answer += 2 ** (i)
    return answer

def flipDigits(string):
    answer = ""
    for letter in string:
        if letter == '0':
            answer += '1'
        if letter == '1':
            answer += '0'
    return answer

f = open(sys.argv[1])
L = []
for item in f:
    L.append(item.strip())

itemLength = len(L[0])

answer = ""

co2Rating = ""
oxygenRating = ""

R = L.copy()
for i in range(0,itemLength):
    # count how many 0's:
    count0 = 0
    # count how many 1's:
    count1 = 0
    for item in L:
        if item[i] == '0':
            count0 += 1
        elif item[i] == '1':
            count1 += 1
    
    if count0 > count1:
        mostCommon = '0'
    else:
        mostCommon = '1'
    
    oxygen = []
    for item in L:
        if item[i] == mostCommon:
            oxygen.append(item)
    if(len(oxygen) == 1):
        oxygenRating = oxygen[0]
    
    L = oxygen.copy()

L = R.copy()
# find CO2
for i in range(0,itemLength):
    # count how many 0's:
    count0 = 0
    # count how many 1's:
    count1 = 0
    for item in L:
        if item[i] == '0':
            count0 += 1
        elif item[i] == '1':
            count1 += 1
    
    if count0 > count1:
        mostCommon = '0'
    else:
        mostCommon = '1'
    
    co2 = []
    for item in L:
        if item[i] != mostCommon:
            co2.append(item)
    if(len(co2) == 1):
        co2Rating = co2[0]

    L = co2.copy()


print("Oxygen Rating:",oxygenRating)
print("CO2 Rating:",co2Rating)
oxygenRating = convertFromBinary(oxygenRating)
co2Rating = convertFromBinary(co2Rating)
print("Oxygen Rating:",oxygenRating)
print("CO2 Rating:",co2Rating)
answer = oxygenRating * co2Rating
print("Answer:",answer)
