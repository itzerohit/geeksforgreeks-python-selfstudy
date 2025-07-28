Power Of Numbers
Difficulty: MediumAccuracy: 20.22%Submissions: 342K+Points: 4
Given a number n, find the value of n raised to the power of its own reverse.
Note: The result will always fit into a 32-bit signed integer.

Examples:

Input: n = 2
Output: 4
Explanation: The reverse of 2 is 2, and 22 = 4.
Input: n = 10
Output: 10
Explanation: The reverse of 10 is 1 (leading zero is discarded), and 10 raised to the power 1 is 10.

Ans -- 

class Solution:
    def reverseexponentiation(self, n):
        # code here
        reverse_n = int(str(n)[::-1])
        
        return n ** reverse_n
        
