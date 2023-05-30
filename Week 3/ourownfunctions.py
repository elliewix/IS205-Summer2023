# let's write a function
# let's call it "say hello"
# it needs a person's name as the input
# it puts that name into a greeting
# it returns that greeting back to the main program

def say_hello(name):
    # do stuff
    greeting = "Hello " + name + "!"
    # return stuff
    # print(greeting)
    return greeting

results = say_hello("coffee")
# print(results)
# print(say_hello("coffee"), say_hello("cat"), say_hello("Elizabeth"))

# def in_to_cm(inches):
#     cm = inches * 2.54
#     return cm # this is the desired
#
# print(in_to_cm(12) + in_to_cm(5))

# HOWEVER if I just printed it

def in_to_cm(inches):
    print(inches * 2.54) # won't be coming out of the funct
    # in a way we can capture
    # if you don't give a return statement
    # NoneType will be returned

results = in_to_cm(12)
print(results)