# If Conditional Statement in python

age = 20

if age >= 18:
    print("Eligible to vote.")

# If else conditional Statements in Python

age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# Short Hand if-else
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")


# elif statement
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 25:
    print("Young adult.")
else:
    print("Adult.")



# Nested if..else conditional Statements in Python
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")



# Ternary Conditional statement in python

# Assign a value based on a condition
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


# Match-Case statements in python
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or three")
    case _:
        print("Other number")

# if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")


# Problem 2: Check if a number is positive
num = int(input("Enter the number: "))
if number >0:
    print("The number is positive. ")



# Problem 3: Check if a student is pass/fail in exam.
num = int(input("Enter the marks: "))
if num >=40:
    print("Pass")
else:
    print("Fail")


# Problem 4: Check if a user has balance to buy an item
balance = int(input("Enter the balance amount: "))
price = int(input("Enter the price: "))
if balance >= price:
    print("Enough funds to complete the purchase")
else:
    print("Price is not enough to complete the purchase")


# Problem 5: Suggest a model of transport based on distance
distance = int(input("Enter the distance you need to travel: "))
if distance <= 2:
    print("Walking")
elif distance <= 5:
    print("Bicycle")
elif distance <= 10:
    print("Bike")
elif distance <= 2:
    print("Bus")
elif distance <= 100:
    print("Car")
elif distance <= 500:
    print("Train")
else:
    print("Plain")

# Problem 6: Battery status
battery = int(input("Enter the batter charge percentage: "))
if battery >= 80:
    print("Full")
elif battery >= 50:
    print("Half")
else:
    print("low")



# Nested if-else statement -- A nested if-else statement places one if inside another to check conditons within conditions. it's useful when a decision depends on a previous condition being true.

# Problem 7: Login with username and password
username = input("Enter the username: ")
password = input("Enter the password: ")

if username == "Rohit":
    if password == "Ram":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Access not granted")



# Problem 8: Check exam pass and scholarship eligibility
marks = int(input("Enter the marks score: "))
passed = int(input("Enter the passing  score: "))
scholarship = int(input("Enter the scholarship criteria: "))
if marks >= passed:
    if marks >= 80:
        print("passed and scholarship will get")
    else:
        print("passed but not eligible")
else:
    print("fail")



# Ternary statement -- The ternary statement provides a shorter way to write if-else statement in a single line

# Problem 9: Check if number is even
number = int(input("Enter the number: "))
print("Even" if number % 2 == 0 else "Odd") 


# Problem 10: Compare two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("First number is greater" if num1 > num2 else "Second number is greater")


# Problem 11: Temperature check :
temp = int(input("Enter the temperatur: "))
print("Hot" if temp >= 30 else "Cool")


# Match-case Statements -- This statement compare a value against multiple patterns, making code cleaner than using many if-elif blocks

# Problem 12: Assign grade
grade = str(input("Enter the grade: "))

match grade :
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case _:
        print("fail")


# Problem 13: Activity Suggestion based on weather condition
weather = input("Enter the wether (sunny/rainy/cloudy/snowy): ")

match weather:
    case "sunny":
        print("Good day gor picnic")
    case "rainy":
        print("Be in room and have a tea")
    case "cloudy":
        print("Go for small walk")
    case "snow":
        print("Go for snow riding")
    case _:
        print("Bad weather")

# Problem 14: Mobile Notification setting based on user profile mode
mode = input("Enter the phone mode (silent/vibrate/loud/do not disturb: ")

match mode:
    case "silent":
        print("Notification are muted")
    case "vibrate":
        print("Notification are on vibrate mode")
    case "loud":
        print("Full sound mode on")
    case "do not disturb":
        print("Everything is muted")
    case _:
        print("Phone switch off")

