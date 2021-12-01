# Creative Part 1

# inputFile = open("three.txt", "r")
# input = ''
# for line in inputFile:
#     #   line_list = line.split()
#     inc = len(line.strip()) + 3
#     input += line.strip()

# inputFile.close()

# count = 0

# print(len(input)/inc)

# i = 0
# while i <= len(input):
#     print(input[i],end = "")
#     if(input[i] == '#'):
#         count += 1
#     i += inc

# print(count)

# Herobrine

inputFile = open("three.txt", "r")

inputList = []
for line in inputFile:
  line_list = line.strip()
  inputList.append(line_list)

inputFile.close()

count = 0

i = 0
for line in inputList:
    while i < len(line):
        print(line[i],end="")
        if(line[i] == '#'):
            count += 1
        if(i + 3 < len(line)):
            i = i + 3
            break
        else:
            i = 3 - (len(line) - i)
            break

print (count)

# 257 is the correct answer for my input