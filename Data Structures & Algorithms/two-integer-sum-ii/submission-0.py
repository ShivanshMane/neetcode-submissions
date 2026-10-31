'''
1) Understanding the problem - 
    1.1 - Input = array of integers numbers and a target
    1.2 - Goal = find the numbers which sums up to the target 
    1.3 - Output = return the indexes of those numbers which sums up to the target
2) Constrainsts - 
    2.1 = what if the array is empty 
    2.2 = what if the array contains just 1 integer
    2.3 = can the integers be negative 
    2.4 = what happens when there's no solution, no numbers which sums up to the target
3) Examples - 
    3.1 - Input: numbers = [1,2,3,4], target = 3, Output: [1,2]
    3.2 - Input: numbers = [], target = 3, Output: []
    3.3 - Input: numbers = [1], target = 3, Output: []
4) Approach - 
    4.1 = Brute Force Approach 
        4.1.1 = First loop selects the first number.
        4.1.2 = Second loop selects the second number, starting from the next position.
        4.1.3 = Check whether their sum equals the target.
        4.1.4 = If it does, return their indices + 1.
        Space Complexity = O(n^2), Time Complexity = O(1)
    4.2 = Optimal Approach 
        4.2.1 = use two pointers, one at the start and second at the end 
        4.2.2 = use while loop to check if l < r 
        4.2.3 = check if the currSum is less than target, if yes increment l by 1
        4.2.3 = check if the currSum is more than the target, if yes decrement r by 1 
        4.2.4 = check if the currSum == target, return the indices, l + 1 and r + 1
        4.2.5 = if no integers found, return empty list
        Space Complexity = O(n), Time Complexity = O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []











        