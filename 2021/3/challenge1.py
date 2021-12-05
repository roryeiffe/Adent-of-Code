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
        answer += '1'
    elif count1 > count0:
        answer += '0'

epsilonRate = answer
gammaRate = flipDigits(epsilonRate)

print("Epsilon Rate:", epsilonRate)
print("Gamma Rate:",gammaRate)

epsilonRateNumber = convertFromBinary(epsilonRate)
gammaRateNumber = convertFromBinary(gammaRate)

print("Epsolon Rate Number:", epsilonRateNumber)
print("Gamma Rate Number:", gammaRateNumber)

print('Final Answer: ', epsilonRateNumber * gammaRateNumber)

    