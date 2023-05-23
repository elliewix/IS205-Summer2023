print("hello") # you need to use print to see the content

# we've seen the = used for variables
name = "Elizabeth"

# == double equals is for equality

# boolean expressions
# smallest piece of stuff you can evaluate that give back
# a True or False

## True and False are boolean objects

True
False

# a small boolean expression
print(5 == 5) # returns True
print(5 == 6) # give false

# student A
has_205 = True
has_203 = False
has_202 = True

# IS999 needs 205 and 203
# IS888 needs one of 203 or 205 plus 202
print("Do they have 205?", has_205 == True)
print("Do they have 203?", has_203 == True)
print("Do they have 202?", has_202 == True)

# you can combine questions
# to get a single answer!
# we can use "and"
print("Can they take IS 999? (need both 203/205", has_205 and has_203)
print("Can they take IS 888? (need one of 203/205) and 202")
print(has_205 or has_203 and has_202) #no
print(  (has_203 or has_205) and has_202  ) #yes, use () to group

# not is tricky....
# not flips a single value
# let's not stress on this one yet
print("Let's print true...", True, "but the opposite is", not True)
print(not has_205)

# Let's start on a conditional block
# meet the 'if' keyword

print("Now for if statments.....\n\n")
# check is999....
# the longer way
#if (has_205 and has_203) == True: # checks if both are true...
# the shorter way....
has_205 = True
has_203 = True
has_202 = False

if has_205 and has_203: # will be false because of 203...
    print("Yes you can take is 999")
else:
    print("No, you can't take 999")

if (has_203 or has_205) and has_202:
    print("you can take IS 888")
else:
    print("no is 888")

# let's talk about elif now......
# we want do do IS 999 and IS 888 but maybe give more info?

# let's add an elif....

has_205 = False
has_203 = False
has_202 = False

if (has_203 or has_205) and has_202:
    print("you can take IS 888")
elif has_202 == False:
    print("you're missing 202")
elif (has_203 or has_205) == False:
    print("you're missing both 203 and 205")
else:
    print("no is 888")


score = 88
if score >= 60:
    print("you pass")
else:
    print("You fail")


score = 88
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


has_205 = True
has_203 = True
has_202 = True

if (has_203 or has_205) and has_202:
    print("you did the thing! take is 999")
    if has_203 and has_205:
        print("and wow you did both!!")
    elif has_205 == False:
        print("but think about taking 205...")
    elif has_203 == False:
        print("but think about taking 203...")
else:
    print("no is 999")


pick_num = 5
fav_num = 7
# check if the num is positive or not

if pick_num >= 0:
    print("positive!")
    if pick_num == fav_num:
        print("and that's the best")
    else:
        print("but that's a bad number")
else:
    print("negative!")


###

num = 500
# check if num above 10 and maybe really big

if num > 100:
    print("greater than 10 also really big!")
elif num > 10:
    print("just over 10")
else:
    print("must be lower than 10")

if num > 10:
    if num > 100:
        print("greater than 10 also really big!")
    else:
        print("just over 10")
else:
    print("must be lower than 10")


# homework 1 tips


hours = 40 # worked in 1 week
wages = 15 # hourly pay
# don't use input() or anything
# change these values around to test


# then do the math....