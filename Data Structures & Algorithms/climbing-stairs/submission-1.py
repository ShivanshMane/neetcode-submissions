'''
Understanding the problem =     
    Input = integer n, representing no of step to reach the top, climb with either 1 or 2
    Goal = count the number of distinct ways to reach the top 
    Output = return the count 
Constraints = can n be 0
            = can n be negative 
            = what is the max value of n 
            = can teh sequence of the steps change( 1+1+2, 2+1+1)
Examples = Input = 2, output = 2 coz  (1 + 1, 2)
         = Input = 4, output = 5 coz  (1 + 1 + 1 + 1, 1 + 1 + 2, 2 + 1 + 1, 2 + 2, 4)
         = Input = 0, output = 1 coz  (take no steps)
Approach = We use bottom-up Dynamic Programming because the number of ways to reach stair n is the sum of the ways to reach stairs n-1 and n-2.
        1. Handle the base cases: n = 1 and n = 2.
        2. Initialize one = 1 and two = 2.
        3. Starting from stair 3, calculate the next answer by adding the previous two.
        4. Update the variables and continue until stair n.
        5. Return two, which contains the final answer. 
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        if n == 2:
            return 2 
        one = 1
        two = 2
        for i in range(3, n + 1):
            current = one + two 
            one = two 
            two = current
        return two

        