'''
Understanding the problem = 
    Input = int array nums, where nums[i] represents amount of money
    Goal = find the maximum amount of money that can be robbed, no adjancent houses
    Output = Return the max money that can be robbed, no adj coz of circle format
Constraints = what if only one integer in array 
            = what is the max length of the integer array
            = what is the max number of houses
            = can integer be negative 
Examples = Input: nums = [3,4,3] ,Output: 4
         = Input: nums = [2,9,8,3,6] ,Output: 15
Approach = we can use dp 
            
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))
    
    def helper (self,nums):
        rob1 = 0 
        rob2 = 0 

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2        