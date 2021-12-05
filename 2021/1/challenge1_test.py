# given a filename, read a file full of numbers and count how many times 
# an increase occurs:
def count_increases(filen):
    """
    Given a filename, read a file full of numbers and count how many times 
    an increase occurs:
    """
    with open(filen, 'r') as f:
        lines = f.readlines()
        count = 0
        for i in range(len(lines) - 1):
            if int(lines[i]) < int(lines[i+1]):
                count += 1
    return count

x = count_increases("input.txt")
print(x)

# given a filename, read a file full of numbers and count how many times
# the sum of each chunk of 3 numbers increases:
def count_increases_chunks(filen):
    """
    Given a filename, read a file full of numbers and count how many times
    the sum of each chunk of 3 numbers increases:
    """
    with open(filen, 'r') as f:
        lines = f.readlines()
        count = 0
        for i in range(len(lines) - 2):
            if int(lines[i]) + int(lines[i+1]) + int(lines[i+2]) < int(lines[i+3]):
                count += 1
    return count

count_increases_chunks("input.txt")
    