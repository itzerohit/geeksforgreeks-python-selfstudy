# Python Data Types
'''1. Numeric -- int, float, complex
2. Sequence Type -- string, list, tuple
3. Mapping Type -- dict
4. Boolean -- bool
5. Set Type - set, frozenset
6. Binary Types - bytes, bytearray, memoryview
 '''

# int, float, string, list and set
x = 50
x = 60.5
x = "Hello World"
x = ["Hello", "World", "Rohit"]
x = ("Hello", "World", "Rohit")

# Numeric Data Types in python
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2+3j
print(type(c))


# Sequence Data Types in Python
'''****  There are several sequences data types of python
* Python String
* Python List
* Python Tuple '''

s = "Welcome to the Geeks World"
print(s)

# Check data types
print(type(s))

# accessing string with the index
print(s[1])
print(s[2])
print(s[-1])



# List Data Types
# Empty List
a = []

# list with int values
a = [1,2,3]
print(a)

# list with mixed int and string
b = ["Geeks",2,3.5]
print(b)
print(b[-1])



# Access List items
a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])



# Tuple Data Type
# Tuples can also be created with a single element, but it is a bit tricky. Having one element in the paranthese is not sufficient, there must be a training 'comma' to make  it tuple


# initiate empty tuple

tup1 = ()

tup2 = ("Geeks", "For")
print("\nTuple with the use of String: ", tup2)


# Access Tuple Items
tup1 = tuple([1,2,3,4,5])
print(tup1[0])
print(tup1[-1])
print(tup1[-3])




# Boolean Data Type in Python
print(type(True))
print(type(False))


# Set Data Type in Python
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)



# Access Set Items
set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")

# check if item exist in set
print("Geeks",  set1)



## Dictionary Data Type
##### Note -- Dictionary key are case sensitive, the same name but different cases of key will be treated distinctly


# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)


# Accessing key - value in Dictionary

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))



# Python Data Type Exercise Questions
#q.1. Code to implement basic list operations
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
fruits.remove("orange")
print(fruits)

#q.2 Code to implement basic tuple operation
coordinates = (3, 5)
print(coordinates)

print("X-coordinates:", coordinates[0])
print("Y-coordinates:", coordinates[1])



# Operators -- These are the special symbols
# Operand -- It is the value on which the opeator is applied

#### Types of Operators in Python
'''1. Arithmetic operator --- +,-,*,/,%
2. Relational operator --- <, <=, >, >=, ==, !=
3. Logical operator -- AND, OR, NOT
4. Bitwise operaor -- &, |, <<, >>, -, ^
5. Assignment operator -- =, +=, -=, *=, %= '''

# Example of Arithmetic Operators in Python:
#variables
a = 15
b = 4

# Addition
print("Addition:", a+b)

# Subtraction
print("Subtraction:", a-b)

# Multiplication
print("Multiplication:", a*b)

# Division
print("Division:", a/b)

# Floor Division
print("Floor Division:", a//b)

# Modulus
print("Modulus:", a%b)

# Exponentiation
print("Exponentiation:", a**b)



# Comparison of Python Operators
a = 13
b = 33

print(a>b)
print(a<b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# Bitwise Operators in python as follow
'''1. Bitwise NOT
2. Bitwise Shift
3. Bitwise ANS
4. Bitwise XOR
5. Bitwise OR'''

a = 10
b = 4
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


# Assignment Operators in Python
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)



# Identity Operators in Python

# is -- True if the operands are identical
# is not -- True if the operands are not identical
a=10
b=20
c=a
print(a is not b)
print(a is c)



# Membership Operators in Python

# in -- True if value is found in the sequence
# not in -- True if value is not found in the sequence

x = 24
y = 20
list = [10,20,30,40,50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")


if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")



# Ternary Operator in Python
## operator that evaluate something based on a condition being true or false
a,b = 10, 20
min = a if a < b else b
print(min)


# Precedence and Associativity of Operators in Python
## Operator precedence and assosiativity determine the priorities of the operator
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0


if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")



# Operator Associativity in Python
print(100 / 10 * 10)
print( 5 - 2 + 3)
print(5 - ( 2 + 3))
print(2 ** 3 ** 2)



# Python Operator Exercise Question

num1 = 5
num2 = 2

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2
remainder = num1 % num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)
    

# code to implement comparison operations on integers
num1 = 30
num2 = 35

if num1 > num2:
    print("The first number is greater.")
elif num1 < num2:
    print("The second number is greater.")
else:
    print("The numbers are equal.")
