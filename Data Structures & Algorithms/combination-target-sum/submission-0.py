'''
Understanding the problem - 
    Input = List of integers, and target(int)
    Goal = form list of integers, whose sum result to target 
    Output = List of list of integers whose sum result to target 
Constraints = Empty list 
            = Can list have negative numbers 
            = what if theres no possible sum which equals to target 
            = can we reuse the same number for sum, if yes how many times
Examples = [1,2,3,6], Output = [[1,2,3]]
         = nums = [3,4,5], target = 16, Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
         = Input:nums = [3] ,target = 5, Output: []
         = Input: nums = [], target = 7, Output:[]
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, current, total):
            # Base case 1
            if total == target:
                res.append(current.copy())
                return
            
            #Base case 2 
            if total > target or i ==len(nums):
                return 
            
            #Include the current number
            current.append(nums[i])
            dfs(i, current, total + nums[i])

            #Backtrack - this pops the last element from current
            current.pop()

            # Skip the current number
            dfs(i + 1, current, total)
        
        #Going inside the dfs method again 
        dfs(0, [], 0)
        return res







        