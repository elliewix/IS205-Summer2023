filename = "Three-years-in-europe.txt"

# using .read()
infile = open(filename, 'r', encoding='utf-8')
text = infile.read() # returns a string of the entire file contents
infile.close()
print(len(text), len(text.split()))

# the for loop pattern

infile = open(filename, 'r', encoding= 'utf-8')

for line in infile:
    # print(line.strip())
    print(line, end = "")
infile.close()

