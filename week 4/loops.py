text = "hello there is a cat"

# when strings loop, it does so by character
# for unicornpoop in text:
#     print(unicornpoop)

# the content of the variable name doesn't matter
# data types don't matter, so long as they are sequences

# for loop asks just one questions:
# 1) what's next?

# the iterable/sequence can say only two things:
# 1) here's the thing! ___
# 2) I'm done.


# for whoknows in 10: # can't do this
#     print(whoknows)

# behind the scenes, ignore this
#
# word = iter("cats")
#
# print(next(word))
# print(next(word))

#######


# import string
#
# print(string.punctuation)
#
# for punc in string.punctuation:
#     print(punc)

# how does .replace() work?

print("original stuff and such", text)

# string methods?
new_text = text.replace("cat", "dog")
print("updated", new_text)

# it can only check one thing at a time....


# iterable updates with replace
# replace all vowels in text with nothing
# require a for loop, .replace, and updating a variable
vowels = "aeiouy"

clean_text = text
for v in vowels:
    # NO! clean_text = text.replace....
    # clean_text = clean_text.replace(v, "_")
    clean_text = clean_text.replace(v, "")
    print(clean_text)

####

# the in keyword
# when used on a string....
# allows us to check if that content is inside the string
# checking substrings
# return True or False
words = "cat dog snake"
other_words = "catastrophe dog"
print("cat" in words) # True
print("dog" in words) # True
print("horse" in words) # False

print("cat" in other_words) # True!

if "cat" in words:
    print("Yes cat found!")
else:
    print("no cat")

#### functions returning true or false

# write a function that checks if only y is a vowel

def check_y(word):
    # return True only if: no vowels plus yes y
    # you: False, my: True
    word = word.lower()
    vowels = "aeiou"
    sometimes = "y"

    result = False
    for v in vowels:
        if v in word:
            result = True

    if (result == False) and (sometimes in word):
        final_result = True
    else:
        final_result = False

    return final_result


print(check_y("you")) # should be false
print(check_y("my")) # should be True


#### hw 2

# yes!
# clean_punc(t1)
# NO!
# clean_punc(t1, t2, t3)
# clean_punc_t1(t1)

# for problem 1....

# def function and stuff
# have the test code

## split!

print(text)
# say I want the words out of text....
# I can use split to get them

words = text.split() # use the default behavior
print(words)

# use the in keyword on the resulting list!
# when you use in keyword on a list, it checks exact match!

print("cat" in words) # true
print("cats" in words) # false
print("the" in words) # false! because it isn't exact match to "there"
# otherwise in words the same, returning true/false
