Factorial
Difficulty: BasicAccuracy: 40.58%Submissions: 178K+Points: 1
Given a positive integer, n. Find the factorial of n.

Examples :

Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120
Input: n = 4
Output: 24
Explanation: 1 x 2 x 3 x 4 = 24
Ans -- 
#User function Template for python3


class Solution:
    def factorial (self, n):
        fact = 1;
        for i in range(1, n+1):
            fact *= i
        return fact
