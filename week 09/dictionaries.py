# dict dictionary
# {} dictionaries
# [] lists
# () tuples or other stray syntax

# we commonly move between str and list
# we just as commonly move between list a dict

# dicts operate and have really distinct syntax

# empty dict
## both of these are the same
d = {}
d = dict()

# the dict contents are key/value pairs
## keys are unique identifiers
## values are the associated values with those keys
## example:  your student id num: your name
## "1234": "Elizabeth"

# make a student dict
# static population, directly adding content
students = {"1234": "Elizabeth",
            "2134": "Phillip",
            "4455": "Fenrir",
            "3122": "Phillip"}

print(len(students)) # length counts by pairs

# get some data out
# lookup by key, content and data type must match!
## literally type it in
## dictvariable[keyvalue]

print(students["3122"])
# print(students[1234]) # key error, because 1234 != "1234"

## use from a variable
## this will be more common because the keys will be coming
## in from data, loops, etc.
stu_num = "3122"
print(students[stu_num])

# can also use the get method
## dict method, 2 args: key and default value
print(students.get("1234", "Missing")) # will give the name
## attempts to get value of key
## will return the default value you provide if it isn't found
## so if it can't find the key, the second arg will be returned

print(students.get(1234, "Missing")) # gives the default value

# that was all to get values out of dicts via a key

print(students)
# could we go from value to key?
# not a direct way

# get all the keys out
## use .keys, but you'll want to recast it to a list
print(list(students.keys()))

# get all the values out
## use .values, but also recast to a list

print(list(students.values()))

# order....

"""
1
2
3
4
..
9
10

1
10
100
2
21
25
3
34
"""

# in 3.9 and later, you can depend on dict order matching in your
# script run.
# BUT one computer to another may have diff orders

# but, it be a bad habit to write code that always depends
# on the order matching

# use this like a "variable" and assign a new value
## update an existing keyvalue pair
## give it the key, set a new value
students["1234"] = "Elizabeth W."

## use the same syntax to add a NEW key/value pair
## put in the new key, and the value
students["9999"] = "Desiree"

print(students)

## loop over content to add into the dictionary
## add these students into the dict, use they key ints to
## generate unique ids
names = ["Aaa", "Bbb", "Ccc", "Ddd"]
keystart = 10000
for n in names:
    key = str(keystart)
    students[key] = n
    keystart = keystart + 1

print(students)

# looping over lists

## there are many ways! But I like this one
## to start with!

## you'll use the .items() method, but there's more
## syntax to go with it
# ## you get key and value by name as variables

for (key, value) in students.items():
    print(key, ":", value)

print(students.items())
## the .items() method returns a list
## where each pair is in a len of 2 tuple the () thing
## the key is always first, the value second

## then it uses multiassignment syntax to break the pairs apart
## so it's doing this but for each pair coming back from the
## dict items list
student_num, stu_name = ('10001', 'Bbb')

print(students)

# dict accum pattern

london = 0
# then you count...
# you're used to this pattern
# but we're extending it! so that we can hold
# multiple counters at the same time, allowing us to add/remove
# them as needed

letter_count = {}

for letter in "phillip": # str will loop over character
    # the in keyword works on dicts, but checks for membership
    # in the keys
    # letter are key, count is values
    if letter in letter_count:
        # increment counter like normal, it just lives
        # in a dict
        letter_count[letter] = letter_count[letter] + 1
        # letter_count[letter] += 1 # just the shorthand
    else:
        # create the counter if that key doesn't yet exist
        letter_count[letter] = 1

print(letter_count)