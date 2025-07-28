### Python Functions -- It is a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function call to reuse code contained in it over and over again

# Benefits of Using Functions
# 1. Code Reuse
# 2. Reduce code length
# 3. Increased readability of code

### Python Function Declaration :
# The syntax to declare a function is:
#   keyword  function name parameter

#def function_name(parameters):
    # statement -- Body of Statement
 #   return expression


### Types of Functions in Python
# Below are the different types of functions in python:
## 1. Built-in library function: These are standard functions in python that are aviable to use.
## 2. User-defined function: We can create our own functions based on our requirements.


# Question -- What is def?
# Ans -- The def keyword stand for define. It is used to create a user-defined function.

## Syntax
#def function_name(parameters):
    # function body


### Explanation:

#1. def: START THE FUNCTION DEFINITION
#2. function_name: Name of the function
#3. parameters: Inputs passed to the function(inside()), optional.
#4. :: Indicates the start of the function body.
#5. Indented code: The function body that runs when called.



# Example:
def fun():
    print("Welcome Rohit")

# above we have just created using the function name

def fun():
    print("Welcome Rohit")
fun() ## This fun function return the value whatever store in the fun ### Calling a function


#### Python Function Arguments

### Syntax for functions with arguments: Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments seprated by a comma.

# def function_name(parameter:data_type)->return_type:
# """Docstring"""
    # body of the function
    # return expression

## Note --  data_type and return_type are optional in function declaration, meaning the same function can also be written as:

def function_name(parameter):
    """Docstring"""
    #body of the function
    return expression

## Let's understand this with an example, we will create a simple function in python to check whether the number passed as an argument to the function is even or odd.
def evenodd(x: int) ->str:
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenodd(16))
print(evenodd(17))



#### THe above function can also e declared without type_hints, like this:
def evenodd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenodd(18))


##### Types of Python function Arguments:
#1. Default argument
#2. Keyword arguments(named arguments)
#3. positional arguments
#4. Arbitrary arguments (variable-length arguments * args and **kwargs)



# 1. Default Arguments : A default argument is a parameter that assumes a default value if a value is not
##### provided in the function call for that argument.

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)



# 2. Keyword Arguments: The idea is to allow the caller to specify the arguments name with values so that the caller does not need to remember the order of parameters.

def student(fname, lname):
    print(fname, lname)

student(fname="Geeks", lname="Practice")
student(lname="Practice", fname="Geeks")



# 3. Positional Arguments: We used the Position argument during the function call so that the first argument is assigned to name and he second argument is assigned to age.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")


# 4. Arbitrary Keyword Arguments -- *args and **kwargs can pass a variable number of arguments to a function using special symbols.

#### 1. *args in python(Non-Keyword Arguments)
#### 2. **kwargs in Python (keyword arguments)


# Example 1: Variable length non-keyword argument
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun("Hello", "Welcome", "to", "GeeksforGeeks")


# Example 2: Variable length keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first="Geeks", mid="for", last="Geeks")





#### Docstring --- This is used to describe the functionality of the function. THe use of docstring in function is optional but it is considered a good practice.

# Syntax can be used to print out the docstring of a function
# print(function_name.__doc__)

# Example 1: Adding Docstring to the function
def evenodd(x):
    """ Function to check of the number is even or odd"""

    if ( x % 2 == 0):
        print("even")
    else:
        print("odd")




print(evenodd.__doc__)




#### Python Functions within Functions:
# A function that is defined inside another function is known S THE INNER FUNCTION OR NESTED FUNCTION .
# Nested function can access variables to the enclosing scope.
# Inner functions are used so that they can be protected from evrything happeining outside of the function.

def f1():
    s = "I love GeeksforGeeks"

    def f2():
        print(s)


    f2()


f1()


#### Anonymous Functions in Python : An anonymous function means that a function is without a name.
# As we already know that def keyword is used to define the normal functions and the lamda keyword is used to create anonymous function

def cube(x): return x*x*x # without lambda

cube_l = lambda x : x*x*x # with lambda

print(cube(7))
print(cube_l(7))



#### Return Statements in Python Function --
# The return, statement in python is used to exit a function and send a value back to the caller.
# It can return any data type, and if multiple values are seprated by the commas, they are automatically packd into a tuple

#### Explantation --
#. return : Ends the functiona and optionally sends a value to the caller.
#. [expression]: Optional value to return, defaults to None if omitted.


### Example -- Python Function Return Statement
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2


print(square_value(2))
print(square_value(-4))


#### Pass by Reference and Pass by Value

# Here x ois a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# aftter function call.

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)



# Example:
def myFun(x):
    x = [20,30,40]


lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)



# Example
def myFun(x):
    x = 20

x = 10
myFun(x)
print(x)



### Exercise -- Try to guess the output of the following code

def swap(x,y):
    temp = x
    x = y
    y = temp

x = 2
y = 3
swap(x,y)
print(x)
print(y)




### Recursive Function in Python --- Recursive in python refers to when a function calls itself. There are many istance when you hvae to build a recursive function to solve mathematical and recursive prolems


def factorial(n):
    if n == 0:
        return 1

    else:
        return n* factorial(n-1)

print(factorial(4))







