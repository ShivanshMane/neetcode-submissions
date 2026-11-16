'''
Understanding the Problem:
- Input: We are given a sorted array that has been rotated at some pivot, along with a target value.
- Goal: Find the index of the target in the array.
- If the target exists, return its index.
- If the target does not exist, return -1.
- We must solve the problem in O(log n) time.

Constraints:
- All integers in the array are unique.
- The array is sorted in ascending order before being rotated.
- The array may contain only one element.
- The array may not be rotated at all.
- The target may or may not exist in the array.

Examples:
1. Input: nums = [4,5,6,7,0,1,2], target = 0
   Output: 4
   Explanation: The target 0 is present at index 4.

2. Input: nums = [4,5,6,7,0,1,2], target = 3
   Output: -1
   Explanation: The target 3 does not exist in the array.

3. Input: nums = [1], target = 0
   Output: -1
   Explanation: The target is not present in the array.

Approach – Modified Binary Search:
1. Initialize two pointers, left and right, at the beginning and end of the array.
2. While left <= right:
   - Calculate the middle index.
   - If the middle element equals the target, return the middle index.
3. Determine which half of the array is sorted:
   - If nums[mid] >= nums[left], the left half is sorted.
   - Otherwise, the right half is sorted.
4. If the left half is sorted:
   - Check whether the target lies between nums[left] and nums[mid].
   - If it does, search the left half by moving right to mid - 1.
   - Otherwise, search the right half by moving left to mid + 1.
5. If the right half is sorted:
   - Check whether the target lies between nums[mid] and nums[right].
   - If it does, search the right half by moving left to mid + 1.
   - Otherwise, search the left half by moving right to mid - 1.
6. If the target is not found after the search, return -1.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r :
            mid = (l+r)//2
            if nums[mid]==target:
                return mid

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1 
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 
                else:
                    r = mid - 1
        return -1
        