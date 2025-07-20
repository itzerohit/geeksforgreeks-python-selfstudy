'''print("Hello,World!")

name = input("Enter your name: ")
print("Hello,", name, "!Welcome!")


# Printing Variables
s = "Bob"
print(s)

# Multiple Variables

s = "Alice"
age = 35
city = "Patna"
print(s,age,city)


# taking two input at a time
x, y = input("Enter two values: ").split() # split method is used to seprate the value of each column 
print("Number of boys: ", x)
print("Number of girls: ", y)


# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


# Taking input as a String
color = input("What color is rose?: ")
print(color)


# Taking input as int
# Typecasting to int
n = int(input("How many roses?: "))  # This process is basically a type casting process
print(n)


## Print Float/Decimal Number in Python
# Taking input as float
# Typecasting to float

price = float(input("Price of each rose?: "))
print(price)


#Find data type of input in python
a = "Hello World"
b = 10
c = 11.22

d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))



#Output Formating
 # Example -- Using Format()
#Example -1 

amount = 150.75
print("Amount: ${:.2f}".format(amount))


#Example -2
#Using sep and end parameter
print("Python", end='@')
print("GeeksforGeeks")


#Seprating with Comma
print('G', 'F', 'G', sep='')

#for formatting a date
print('09', '12', '2016', sep='_')

# another example
print('pratik', 'geeksforgeeks', sep='@')

#Using f-string
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


#Using % Operator
1. %d -- integer
2. %f -- float
3. %s -- string
4. %x -- hexadecimal
5. %o -- octal


# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

print("The sum is %d" %add)


#Taking Conditional User Input in Python

* input() is used to take user input as a string
* You can use int() or float() to convert it if needed
* Taking multiple input
* Taking Conditional User Input
* How to take integer input
* Get a String as input from user
* Format()
* sep and end parameter
* f-string
* % Operator




## Python Variables -- Variables act as placeholder for data. They allow us to store and reuse values in our program

#variable 'x' stores the integer value 10
x=10
# variable 'name' stores the string "Samantha"
name = "Samantha"

print(x)
print(name)'''


'''
# Multiple assignments
#1. Assigning the same value
a = b = c = 100
print(a, b, c)

#2. Assigning Different Value
a , b, c = 1,2.5,"hello"
print(a,b,c)


# Typecasting
s = "10" # Initially a string
n = int(s)
print(n)
cnt = 5
n = float(cnt)
print(n)
age = 22
s2 = str(age)
print(s2)

# Getting the Type of Variable
# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1,2,3]
d = {'key':'value'}
bool = True
print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))


# Assigning value to variable
x = 10
print(x)

# Removing the variable using del
del x

# 1. Swapping Two Variables
a, b = 5, 10
a, b = b, a
print(a,b)

# 2. CountingCharacters in a String
word = "python"
length = len(word)
print("Length of the word is:",length)

# 2. Scope of a Variable
#the scope of a variables define where it can be accessed in the program. There are two main types of scope: local and global

#1. Local variable -- Defined within a function or block, accessible only inside that loop
#2. Global Variable -- Defined outside functions, accessible throughout the program 
'''

# Notes
'''

# 1. Getting List of all Python keywords
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


🔑 Python Keywords – Quick Notes
Reserved words with special meaning in Python.

Can’t be used as variable, function, or class names.

Use import keyword → keyword.kwlist to view all.

✅ Categories of Keywords
Value: True, False, None

Operators: and, or, not, is, in

Control Flow: if, else, for, while, break, continue, pass, try, except, raise, finally, assert

Functions/Classes: def, return, lambda, yield, class

Context: with, as

Import: import, from

Scope: global, nonlocal

Async: async, await

❌ Error Example
python
Copy code
for = 10  # ❌ SyntaxError – can’t use keywords as variable
🆚 Keywords vs Identifiers
Keywords: Reserved (e.g., if, while)

Identifiers: User-defined (e.g., x, sum)

'''
