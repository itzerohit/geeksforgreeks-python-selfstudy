### Python Pass Statement
# Example Use of Pass Keyword in a Function
def fun():
    pass # Placeholder, no functionality yet

# call the function
fun() # Function fun() is defined but contains the pass statement, meaning it does nothing when called.
# program continue execution without any errors and the message is printed after calling the function


#### Using pass in Conditiona; statements

x = 10

if x > 5:
    pass # placeholder for future logic
else:
    print("x is 5 or less")
    
    
### USing pass in Loops -- In loops(such as for or while), pass can be used to indicate that no action is required during iterations.

for i in range(5):
    if i == 3:
        pass # Do nothing when i is 3
    else:
        print(i)
### Using pass in Classes -- In classes, pass can be used to define an empty class or a placeholder for method that we inteded to implement later,


class EmptyClass:
    pass # No method or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    def greet(self):
        pass # Placeholder for great method


# Creating an instance of th class
p = Person("Anurag", 30)







##### Global and Local Variables in Python -
# In Python, global variable are declared outside any function and can be accessed anywhere in the program, includinginside function.
# On the other hand, local variables are created within a function and are only accessibleduring that function's execution.
# This means local variable exist only inside the function where they are defined and cannot be used outside.


### Python Local Variables --
# 1. Local variable are created within a function and exist only during its execution. they are not accessible from outside of the function.

### Example : In this example, we are creating and accessing a local variable inside a function.

def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()  ### We define greet() with a local variable msg and print it. Since msg exists only during the function's execution, it's accessed within the function.
# Calling greet() displays the message


### Example : In this example, we are creating a local variale innside  a function and then trying to access it outsidethe function, which causes an error.
def greet():
    msg = "Hello!"
    print("Inside function:", msg)

greet()



### Python GLobal Variables:
# Global variables are defined outside all functions. They can be accessed and used in any part of the program, including inside functions.

# Example 1: In this example, we are creating a gloabal variable and then accessing it both inside and outside the function.

msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)


# Example 2: In this example, we're creating a gloabal variable and then using it both inside and outside a function.

def fun():
    print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
fun()
print("Outside Function", s)


### Note -- As there are no locals, the value from the globals will be used but make sure both the local and the global variables should have same name.


###### -- Why do we use Local and Global variables in Python?
# If a variable is defined both globally and locally with the same name, the local variable shadows the global
# variable inside the function. Changes to the local variable do not affect the global variable unless you explicit declare the variable as global.


def fun():
    s = "Me too."
    print(s)


s = "I love Geeksforgeeks"
fun()
print(s)



##### What ifWe try to modify a global variable inside a function?
# Ans -- Attempting to change a global variable inside a function without declaring it as a global will cause an error
##### So that TO modify a global variable inside a function, you must explicitly tell python that yo want to use the global version by using the global keyword.


def fun():
    global s
    s += 'GFC' # Modify the global variable
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)


s = "python is great!"
fun()
print(s)




### Example 2: This example demonstrates how python handles global and local variables with the same name, and how the global keyword affects their behaviour.


a = 1 # GLobal vaiable

def f():
    print('f():',a) # use global a

def g():
    a = 2 # local variable shadows global
    print('g():',a)

def h():
    global a
    a = 3 # modifies global a
    print('h():', a)


print('global:', a)
f()
print('global:', a)
g()
print('global:', a)
h()
print('global:', a)




#### Difference b/w local and global variable
'''
Comparison basis	Global Variable	Local Variable
Definition	Declared outside the functions	Declared within the functions
Lifetime	They are created  the execution of the program begins and are lost when the program is ended	They are created when the function starts its execution and are lost when the function ends
Data Sharing	Offers Data Sharing	It doesn't offers Data Sharing
Scope	Can be access throughout the code	Can access only inside the function
Parameters needed	Parameter passing is not necessary	Parameter passing is necessary
'''
