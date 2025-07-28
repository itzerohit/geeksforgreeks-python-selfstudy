Subset Sums
Difficulty: MediumAccuracy: 72.55%Submissions: 168K+Points: 4
Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.

Examples:

Input: arr[] = [2, 3]
Output: [0, 2, 3, 5]
Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2. When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.
Input: arr[] = [1, 2, 1]
Output: [0, 1, 1, 2, 2, 3, 3, 4]
Explanation: The possible subset sums are 0 (no elements), 1 (either of the 1's), 2 (the element 2), and their combinations.
Input: arr[] = [5, 6, 7]
Output: [0, 5, 6, 7, 11, 12, 13, 18]
Explanation: The possible subset sums are 0 (no elements), 5, 6, 7, and their combinations.

Ans --- 

class Solution:
	def subsetSums(self, arr):
		# code here
		result = []
		
		def solve(index, current_sum):
		    if index == len(arr):
		        result.append(current_sum)
		        return
		    
		    
		    solve(index + 1, current_sum + arr[index])
		    
		    solve(index + 1, current_sum)
		    
	    solve(0, 0)
	    return result
		 
