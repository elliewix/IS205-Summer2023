print() # can run with no input
print("hello!") # or run with input
print("hello!", 10 * 34) # or with many things
# every function is designed to work in a diff way

# you'll always have a name for the function
# and it'll always be followed by () to make it work
# this is "calling" a function
# means to ask the function to work/execute by name()

print( min(100, 1,4,9) )

# inputs when calling...
# you ask the function to work, give it something to work with
# the stuff in the () are the: inputs, parameters, or arguments
# 100, 1,4,9 is the input for max

print( max(100, 1,4,9))

# stuff gets sent into a function
# function cranks on it, doing whatever it was
# programmed to do
# value(s) get returned from the function back to the
# main main program, and this is the result we see

# in python, ALL functions return something

# many times we just use functions as they exist, the tools
# already made for us, many just ready to go

# built in functions vs std lib functions
# built in ones are ready to use all the time
# we need to "import" the std lib ones

# importing functions

# to me, library/module are the same thing

# to use something like the math module
# or something else from the std lib, you need to import
# I use the most conservative way
# but community convention always wins

# eg import pandas as pd, this is a way to import with shorthand
# and when you see official docs doing it that way, you match it

# otherwise, do it way I show you

# import _module name_

import math
# now req you to say math.function()

print(math.sqrt(9))

