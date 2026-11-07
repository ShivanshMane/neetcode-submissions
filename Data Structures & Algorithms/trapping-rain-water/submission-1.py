'''
1) Understanding the problem -
    1.1 = Input = Array of non-negative integers representing bar heights.
    1.2 = Goal = Calculate the total amount of rainwater trapped between the bars.
    1.3 = Output = Return the total amount of trapped water as an integer.
2) Constraints -
    2.1 = What if the array is empty?
    2.2 = What if no water can be stored?
    2.3 = What is the maximum length of the array?
    2.4 = Can the array contain zeros? Yes.
    2.5 = Can the heights be negative? No.
3) Examples -
    3.1 = Input: height = [0,2,0,3,1,0,1,3,2,1]
         Output: 9
    3.2 = Input: height = [3,0,2]
         Output: 2
    3.3 = Input: height = [1,2,3,4]
         Output: 0
         Explanation: Water cannot be trapped because the bars
         keep increasing.
4) Approach - 
    4.1 = Brute Force Approach 
        4.1.1 = Find the maximum height on the left side, including the current index.
        4.1.2 = Find the maximum height on the right side, including the current index.
        4.1.3 = The water level is the minimum of these two maximum heights.
        4.1.4 = Subtract current bar's height to calculate the trapped water at that index
        4.1.5 = Add the trapped water to the total.
        4.1.6 = Return the total after checking every index.
        Space Complexity = O(1), Time Complexity = O(n^2)
    4.2. = Optimal Approach 
        4.2.1 =Initialize two pointers, l and r, one at the beginning and one at the end of the array.
        4.2.2 = Initialize leftMax and rightMax using the heights at the two pointers.
        4.2.3 = Initialize res = 0 to store the total trapped water.
        4.2.4 = Run a while loop as long as l < r.
        4.2.5 = Compare leftMax and rightMax:
            4.2.5.1 = If leftMax is smaller:
                  - Increment l by 1.
                  - Update leftMax using max().
                  - Calculate trapped water using leftMax - height[l].
                  - Add it to res.
            4.2.5.2 = Decrement r by 1.
                    - Update rightMax using max().
                    - Calculate trapped water using rightMax - height[r].
                    - Add it to res.
        4.2.6 = Return res after the loop finishes.
        Time: O(n), Space: (O1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        
        