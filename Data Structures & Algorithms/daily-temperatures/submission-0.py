'''
Understanding the problem = 
    Input = given an array of integers temperatures
    Goal = build an array result, where result[i] is number of days, day before warmer temp
    Output = return the array 
Constraints =  
    1 <= temperatures.length <= 100,000
    30 <= temperatures[i] <= 100
    The array contains at least one temperature.
    If no warmer temperature exists in the future, return 0
Examples = Input: temperatures = [30,38,30,36,35,40,28], Output: [1,4,1,2,1,0,0]
         = Input: temperatures = [], Output: []
         = Input: temperatures = [30], Output: [0]
Approach = Optimal using stack 
         = 1. Initialize a result array with 0s, same length as temperatures.
           2. Initialize an empty stack to store (temperature, index) pairs.
           3. Iterate through the temperatures array using enumerate().
        4. If the stack is not empty and the current temperature is greater than the temperature at the top of the stack:
           4.1 Pop the top pair from the stack.
           4.2 Calculate the number of days waited (current index - previous index).
           4.3 Update the result array at the previous index.
           4.4 Repeat until the stack is empty or the current temperature is not greater.
        5. Push the current (temperature, index) pair onto the stack.
        6. Return the result array.
        Time Complexity = O(n), Space Complexity = O(n)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t,i))
        return res
        