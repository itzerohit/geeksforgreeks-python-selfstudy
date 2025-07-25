# For loops in python -- For loops is used to iterate over a sequence such as a list, tuple, string or range. it allow to execute a block of code repeatedly, once for each item in the sequence.

n = 4
for i in range (0,n):
    print(i)
# IterTING OVER LIST, TUPLE, STRING AND DICTIONARY USING FOR LOOPS IN PYTHON
li = ["geeks", "for", "geeks"]
for i in li:
    print(i)

tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)

s = "Geeks"
for i in s:
    print(s)


d = dict({'x':123, 'y':354})
for i in d:
    print(d)

set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)


# Iterating by the index of sequences
li = ["geeks", "for", "geeks"]
for index in range(len(li)): # The range(len(list)) generates indices from 0 to the length of the list minus 1.
    print(li[index])

## Using else statement with for loop in python
li = ["Geeks","for", "geeks"]
for index in range(len(li)):
    print(li)
else:
    print("Inside else block")




#### While loop in python -- A while loop is used to execute a block of statements repeatedly until a given condition is used.
# When the condition is false the line immediatley after the loop of the program is executed.


cnt = 0
while (cnt < 3):
    cnt = cnt+1
    print("Hello Geek")
    
## Using else statement with while loop in python

#while condition:
    # executes these statements
#else:
    # executes these statements

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In else block")



## Nested Loops in Python -- python programming language allows to use one loop inside another loop which is called nested loop.
### The syntax for a nested while loop statement in the python programming

#while expression:
#    while expression:
#        statement(s)
#   statement(s)


for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


## Loop Control Statements
# Continue Statements -- The continue statement in python returns the control to the beginning of the loop

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue                        ### Here the continue statement is used to skip the current iteration of a loop and move to the next iteration.
    print('Current Letter :', letter)




## Break Statement -- The break statement in python brings control out of the loop.
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter : ', letter)




