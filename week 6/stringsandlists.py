infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
# not .read() this time!
lines = infile.readlines() # returns a list of strings
infile.close()

# print(lines)

# the [] means we are working with a list
# [], but on their own
# lists are a container data type, used to hold stuff

# lists hold stuff in order
# in lines, the lines are held in order and order saved

# lists grow or contract in size as needed
# don't call them arrays!

# readlines, goes from top to bottom in a file
# returns a list containing each line as a string, in sequence

# lists contain elements in sequence

# there's all kinds of stuff you can do to a list!

# working with lists, briefly

## Let's do something smaller

## let's split a string apart!

some_text = 'The       Project Gutenberg eBook, Three Years in Europe, by William Wells\n'

## .split in more detail: a string method, use the default args, and makes a list

words = some_text.split()
# by default, (), breaks text apart based on groups of consecutive white space
print(words)

# so to loop over words in a line, you use .split() and loop over the result

for w in words:
    print(w)

# you have to isolate the line first

# for l in lines:
#     # so l is the line of text
#     print(l.split()) # so you can call split on l
#

# cleaning more words, using strip

## .strip() is another string method

import string

# strip acts on the left and right side of a string
# removing any instances of what you've given it
# it keeps removing stuff until it hits something it doesn't match
print("__*cat's*__".strip("_"))
print("__*cat's*__".strip("*")) # nothing will happen here
print("__*cat's*__".strip("_*")) # removes both the order doesn't matter
print("__*cat's__*__".strip("_*")) #same behavior

# allows us to clean the outside but not touch the inside
# as soon as it sees something not to be removed, it stops looking
print("_(-,'_*cat's*_'''_".strip(string.punctuation))

# how do we save all these cleaned words? list accumulator
cleaned_words = [] # create base, an empty list
for w in words:
    cleaned_w = w.strip(string.punctuation)
    # print(cleaned_w)
    cleaned_words.append(cleaned_w) # no assignment! mutates the list
    # print(words)
    # print(cleaned_words)

print("eBook" in words) # False
print("eBook" in cleaned_words) # True

## putting more of this together.....

# for loop going over each line, making: line
    # so imagine all the stuff we just did about cleaning the lines
    # but contained inside another for loop
    # split line apart, makes: words
    # for loop going over the list of words, making: word

# except! we are putting the cleaning stuff in a function
# lets us skip a nested loop

# this is more like hw3
# for loop going over the lines....
    # pass each line into your function
    # get results back.....
    # do stuff about it

######

# so now we check for things, we also want to write out the results

# which involves writing files

# new file name you just make as a string!
outfile = open("outputlines.txt", "w", encoding="utf-8")
# just to test....
#outfile.write("hello there humans") # use .write!
for l in lines:
    char_count = len(l)
    output_content = str(char_count) + " " + l
    outfile.write(output_content)
outfile.close()

####

term = "boat"

filename = term + "-results.txt"

print(filename)
# then do your outfile using filename....

#for l in lines:
    # call function with line and term....
    # check
        # write stuff