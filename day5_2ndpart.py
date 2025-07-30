### *args and **kwargs in Python:
# In Python *args and **kwargs are used to allow functions to accept an arbitrary number of arguments. These features provide
    # great flexibility when designing functions that need to handle a varying number of inputs.


# *args example
def fun(*args):
    return sum(args)


print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))


# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)


fun(a=1, b=2, c=3)



#### There are two special symbols to pass multiple arguments:

# Special symbols used for passing arguments
#### THere are basically two types of special symmbols
##### 1. Keyword Arguments 2. Non-Keyword Arguments

### Special Symbols Used for passing arguments  in python:
# *args(Non-Keyword Arguments)
# **kwargs(eyword Arguments)

## Note : "We use this "wildcard" or "*" notation like this - *args OR **kwargs - as our function's argument when we have doubt anout the number of arguments we should pass in a function.

# Python *args --
## The special suntax *args in function definitions is used to pass a variable number of argument in location.
# It is used to pass a non-keyword, variable-length argument list.
# These arguments are grouped into a tuple, allowing the function to hande any number of inputs.

## for example, a multiply() function can use *args to accept any number of inputs
# and multiply them. The *makes the variable iterable, so it can be looped through or used with functions like map() and filter()

## Example 1: Python program to illustrate *args for a variable number of arguments

def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


## Example 2: Python program to illustrate *args with a first extra argument.

def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)


fun("Hello", "Welcome", "to", "GeeksforGeeks")




### Python **Kwargs -- The special syntax **kwargs in function definitions is used to pass a
# variable length argument list. We use the name kwargs with the double star**.

# * A keyword argument is where you provide a name to the variable as you pass it into the function.
# * It collects all the additional jeyword arguments passed to the function and stores then in a dictionary.


