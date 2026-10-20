'''
Understanding the problem =    
    Input - int array nums, where nums[i] represent amount of money ith house has
    Goal = rob money from houses, robbing from adjacent houses not allowed 
    Output = return the max money robbed, basically sum of integers, adjacent not allowed
Constraints = what is array is empty 
            = can the integers be negative 
            = can it contain only 1 integer 
            = what is the max length of nums, nums[i]
Examples = Input = nums = [1,2,3], Output = 4, coz 1 + 3 = 4
         = Input = nums = [1,2,3,4,5], Output = 9, coz 1 + 3 + 5 = 9
         = Input = nums = [1,], Output = , coz 0 + 1 = 1
Approach = we can use dynamic programming to calculate the initial values, and then use it afterwards 
         = 
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i - 2])
        return dp[-1]
        