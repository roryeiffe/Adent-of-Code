# read a file and return a list of lines converted to integers
def read_file(filen):
    with open(filen, 'r') as f:
        return [int(line) for line in f.readlines()]