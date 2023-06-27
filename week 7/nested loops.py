words =  ['cat', 'dog', 'snake']
letters = ['a', 'o', 'y']
# okay....
# for each letter, which words have them?
# which words have each letter?
# are there any letters that don't appear?
# given how much we are talking about it
# let's make letters the outside loop

# loop over individually....
# for w in words:
#     print(w)
# for l in letters:
#     print(l)
# but to put it together, we need a nested loop

# for w in words: # outer loop
#     for l in letters: # inner loop
#         print(w, l)
#         # print(l, w)
#
# for l in letters: # outer loop
#     for w in words: # inner loop
#         print(l, w)


# outer loop will traverse once
    # inner loop will traverse once for each outer item

# when does this matter?
## not always!
## When you have something that can only traverse once,
## like a file to read in, or file to write out, etc.
## when you need one the things to all stay together and
## the loop not reset for it


# let's add some logic!

# for l in letters:
#     for w in words:
#         if l in w:
#             # print(l, l in w)
#             print(l, w) # print off just the True cases


# let's add a boolean flag to tell us if each
# letter was found or not
for l in letters:
    letter_found = False
    for w in words:
        if l in w:
            # print(l, l in w)
            # print(l, w) # print off just the True cases
            letter_found = True # flip the flag
    # print(l, letter_found)

# let's print out just the negative cases for the letters
# add a counter to count how many letters not found

not_found_letter = 0
for l in letters:
    letter_found = False
    for w in words:
        if l in w:
            letter_found = True # flip the flag
    if letter_found == False:
        not_found_letter = not_found_letter + 1
        print(l, letter_found)

print(not_found_letter, "letters were not found")

# let's talk about files

## think about the outfile = .... as the "base"
## and using .write() or whatever as the incrementation
## and then close() will be after the incrementation in done

words = ["cat", "dog", "snake", "horse", "viper"]

for w in words:
    # when you are working on making a outfile
    # with some variable content,
    # always! print out the string before anything else!
    # remember that file names are strings!
    # print(w + "-wordresults.txt") # change print to your outfile
    outfile = open(w + "-wordresults.txt", 'w', encoding = 'utf-8')
    outfile.write(w + " is a word")
    outfile.close()

# outfile is generally the outer loop
# the inner loop generally controls the content going into the outfile

for w in words:
    outfile = open(w + "-wordresults.txt", 'w', encoding = 'utf-8')
    # outfile.write(w + " is a word")
    # if letter in the word,
    # write the letter to the file with a note
    for l in letters:
        if l in w: # true that letter in there
            outfile.write(l + " is in there\n")
        else:
            outfile.write(l + " in NOT in there\n")
    outfile.close()

# write out a file with the letter and the words that contain it

words.append("horsey")

for l in letters:
    outfile = open(l + "-words.txt", 'w', encoding='utf-8')
    for w in words:
        if l in w:
            outfile.write(w + '\n')
    outfile.close()

