import sys

# To use this in different file director:
# import sys
# sys.path.insert(1, 'path to this file from there')
# import utils

def parse_file():
	L = []
	filen = sys.argv[1]
	f = open(filen,"r")
	for item in f:
		L.append(item.strip())
	return L
