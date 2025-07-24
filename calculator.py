Given two numbers a and b; you need to perform basic mathematical operation on them. You will be provided an integer named as operator. 
If operator equals to 1 add a and b, then print the result as a string.
If operator equals to 2 subtract b from a, then print the result as a string.
If operator equals to 3 multiply a and b, then print the result as a string.
If operator equals to any another number, print "Invalid Input"(without quotes).
Note: Do not add a new line at the end

Examples:

Input: a = 1, b = 2, opr = 3
Output: 2
Explanation: 1 * 2 = 2
Input: a = 2, b = 2, opr = 2
Output: 0
Explanation: 2 - 2 = 0
Constraints: 

Ans --- 
def utility(a, b, operator):
    if operator == 1:
        result = a + b
        print(str(result), end="")
        
    elif operator == 2:
        result = a - b
        print(str(result), end="")
    elif operator == 3:
        result = a * b 
        print(str(result), end="")
    else:
        print("Invalid Input", end="")
        
