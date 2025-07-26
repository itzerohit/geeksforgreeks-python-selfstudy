
## Let's Do some practice question based on above topic

# problem 1: This Python code iterates through a list called fruits, containing "apple",
# "orange" and "kiwi." It prints each fruit name on a separate line, displaying them in the
# order they appear in the list.

fruits = ["apple","orange","kiwi"]
for i in fruits:
    print(i)

# problem 2: This Python code manually iterates through a list of fruits using an iterator. It
# prints each fruit's name one by one and stops when there are no more items in the list.

fruits = ["apple","orange","kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

# problem 3: The problem is to take shopping items as input from the user and display them one by one in a structured format.

items = input("Enter shopping items seprated by commas: ").split(',')

for i in items:
    print("Buy: ",i.strip())


# problem 4: Print squares of number from 1 to n
# Display the square of each number starting from 1 up to a number provided by the user.

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("Sqaure of",i,"is",i**2)
    


### While Loop -- A while loop continues to execute as long as a given condition remain true. It's
#especially useful when the number of iteration is unknown in advance and depends on dynamic conditions

# Problem 1: Countdown timer
# Implement a countdown that starts from a user-given number and decreases to 1, displaying the remaining time at each step.

seconds = int(input("Enter the number of seconds you want: "))

while seconds > 0:
    print("Time remaining: ", seconds)
    seconds -= 1  # This is the very important step


# Problem 2: Sum until user enters 0
total = 0
num = int(input("Enter number (0 to stop): "))
while num!= 0:
    total += num
    num = int(input("Enter number (0 to stop): "))
print("Total sum:", total)



### Nested loop[ --
# Problem 1: Print a multiplication table
n = 3
for i in range(1, n+1):
    for j in range(1, 11):
        print(i*j, end = '')
    print()

# Problem 2: Print identity matrix pattern
n = 4

for i in range(n):
    for j in range(n):
        if i == j:
            print("1", end = " ")
        else:
            print("0", end = " ")

    print()


### Control Flow Statements in Loops

# 1. break

# Problem 1: Stop printing at a target item
items = ["Apple", "Banana", "Cat", "Dog"]
for i in items:
    if i == "Cat":
        break
    print("Item: ",i)


# Problem 2: Find first even number
while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("First even number found:", num)
        break


# 2. continue -- The continue statement skips the current loop iteration and moves to the next one.

# Problem 1: Skip out of stock items
items = ["milk", "bread", "out of stock", "eggs"]

for i in items:
    if i == "out of stock":
        continue
    print("Buy:",i)


# Problem 2: Skip the even numbers:
n = 10

for i in range(n):
    if i % 2 == 0:
        continue
    print("Odd number:",i)



# 3 . pass -- The pass statement does nothing. It's a placeholder when the syntax requires a statement but no action is needed

# Problem 1: Loop through a list of tasks and use pass where logic is yet to be added,keeping the loop valid.

tasks = ["email", "meeting","call"]

for i in tasks:
    if i == "call":
        pass
    print("Do:",i)


# Problem 2: Write a loop structure that currently performs no action but is kept for future use a pass statement

for i in range(5):
    pass # Placeholder for future logic

