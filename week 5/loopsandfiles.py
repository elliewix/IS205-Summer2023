text = "this is some text"

# unpacking loop
# take content, and isolate indiv pieces
# remeber the content in unpacking itself

# for character in text:
#     print(character)

# repetition loop
# saying, do this thing some number of times
# can be static, like 5 every time
# can be relative, depending on the size of something

## say "happy birthday" once for each year you are old
## so, 5 times if you are five...etc.

age = 3
# we'll use the range(...) function in the loop

for i in range(age):
    print("happy birthday!")

print(list(range(age)))

# working with range

# range(10) this is like range(stop) like a stop value...
# goes up to but not including that stop value

# range(start, stop)
# start is inclusive, stop is exclusive

print(list( range(10, 13) )) # gives me 10,11,12

for i in range(10, 13):
    print("happy birthday again!")

# there's also range(start, stop, step) which we won't use

# print(list( range(0, 10, 2) ))

# you can do math to i, usually to offset it
for i in range(5):
    print("happy birthday " + str(i + 1) + " year(s)!")
    # print("stuff", i) recasts for free
    # but can't save that result to a variable

# so this is sort of repetition + unpacking
# these categories are just for organization and not science

# you can use something other than i....
# what my 7yo would do
for fart in range(5):
    print("hello " + str(fart))

print(len("cats"))

for i in range(len("cats")): # can also be based on length
    print("cat", i)

#####

# counters! accumulators, etc.

# counters used to count things up, usually by 1s
# usually like the same number each round

# accumulators.... used to sum things
# get the sum total of certain values
# or to collect up variable values from somewhere else

# the five steps.....

# count the letters in a word or string...
# yes I could use len, but we're practicing a pattern
# and we'll make more complex later

# 1 goes outside of and before your for loop
count = 0 # 1, establish your base, usually 0 for ints
for letter in "cats": # unpacking loop, 2: loop!
    # 3: do your business, whatever
    # 4: decide what to increment and where, for a counter, just add 1 to the base
    # 5: increment your base
    count = count + 1 # count++, not a thing in python
    # shorthand, count += 1 but you'll be use it the long way

# secret 6.... print the final result!
# outside of and after your loop, print the base
print("final count is", count)

# count all the vowels in a string

vowels = "aeiou"
count = 0

for character in "here's is some text":
    if character in vowels: # 3, doing business
        count = count + 1

print("number of vowels", count)

#### add more??

import string
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
spaces_count = 0

for character in "here's is some text":
    if character in vowels: # 3, doing business
        vowel_count = vowel_count + 1
    elif character in string.ascii_lowercase:
        consonant_count = consonant_count + 1
    elif character == " " or character in string.punctuation:
        spaces_count = spaces_count + 1
    else:
        print("this should never print", character)

print("number of vowels", vowel_count)
print("number of consonants", consonant_count)
print("number of spaces", spaces_count)

print(len("here's is some text"), vowel_count + consonant_count + spaces_count)


