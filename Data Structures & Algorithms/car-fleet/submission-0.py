'''
Understanding the problem - 
    Input = Target, Position, and speed of the car
    Goal: Determine how many different car fleets will arrive at the destination
    Output: Return an integer representing the total number of car fleets
Constraints = 
    1 <= n <= 100,000
    0 < target <= 1,000,000
    1 <= speed[i] <= 1,000,000
    0 <= position[i] < target
    All starting positions are unique.
    Cars cannot overtake one another.
    A faster car catching up to a slower car must travel at the slower car's speed
Examples = Input: target = 10, position = [1, 4], speed = [3, 2], Output: 1
         = Input: target = 10, position = [4, 1, 0, 7], speed = [2, 2, 1, 1], Output: 3
Approach = Optimal - Using stack 

'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []
        for p, s in pairs:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)


        