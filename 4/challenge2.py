import sys
class attribute:
	def __init__(self,key,value):
		self.key = key
		self.value = value
	def __str__(self):
		return self.key + ":" + self.value



f = open(sys.argv[1],'r')
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

newpassports = []
count = 0
# loop through passports:
for passport in passports:
	attributes = dict()
	for att in passport:
		L = att.split(":")
		attributes[L[0]] = L[1]
	valid = 0
	if "byr" in attributes:
		birth_year = int(attributes["byr"])
		if birth_year >= 1920 and birth_year <= 2002:
			print("byr valid")
			valid += 1
	if "iyr" in attributes:
		issue_year = int(attributes["iyr"])
		if issue_year >= 2010 and issue_year <= 2020:
			valid += 1
			print("iyr valid")
	if "eyr" in attributes:
		exp_year = int(attributes["eyr"]) 
		if exp_year >= 2020 and exp_year <= 2030:
			valid += 1
			print("eyr valid")
	if "hgt" in attributes:
		height = attributes["hgt"]
		units = height[-2:]	
		number = height[:-2]
		if number.isnumeric():
			height = int(number)
			if units == "in":
				if height >= 59 and height <= 76:
					valid += 1
					print("hgt valid")
			elif units == "cm":	
				if height >= 150 and height <= 193:
					valid += 1
					print("hgt valid")

	if "hcl" in attributes:
		hair_col = attributes["hcl"]
		if hair_col[0] == "#" and len(hair_col) == 7:
			hair_valid = True
			for letter in hair_col[1:]:
				if letter not in ["0","1","2",'3','4','5','6','7','8','9','0','a','b','c','d','e','f']:
					hair_valid = False
			if hair_valid:
				valid += 1
				print("hair valid")
	if "ecl" in attributes and attributes["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		valid += 1
		print("ecl valid")
	if "pid" in attributes:
		pid = attributes["pid"]
		if pid.isnumeric():
			print(pid)
			if len(pid) == 9:
				valid += 1
				print("pid valid")
	if valid >= 7:
		count += 1
	print()

print(count)






	
	



