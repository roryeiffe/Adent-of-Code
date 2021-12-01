f = open("input.txt",'r')
L = []
for item in f:
	L.append(item.strip())
# Construct arrays of possible keys:
creden =       ["ecl","eyr","hcl","byr","iyr","pid","hgt"]
creden_plus =  ["ecl","eyr","hcl","byr","iyr","pid","hgt","cid"]
creden.sort()
creden_plus.sort()

# stores all passports
passports = []
# stores key-value pairs (in string form):
passport = []
for item in L:
	# if empty line, append passport, and reinitialize passport variable:
	if item == "":
		passports.append(passport)
		passport = []
	# otherwise, loop through current line and append
	# key value pairs to passport
	items = item.split(" ")
	for att in items:
		if att != "":
			passport.append(att)
# grab the last passport
passports.append(passport)

print(passports)

count = 0
# loop through passports:
for passport in passports:
	keys = []
	# extract out the keys:
	for att in passport:
		keys.append(att.split(":")[0])
	# sort them
	keys.sort()
	# see if keys are valid:
	if keys == creden or keys == creden_plus:
		count += 1

print(count)



