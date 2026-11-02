'''
1) Understanding the problem - 
    1.1 = Input = Array of strings token, valid arthmetic expression in reverse notation
    1.2 = Goal = find the integer that represents the arthmetic expression 
    1.3 = Output = return the integer which represents the arthmetic expression
2) Constraints - 
    2.1 = what if the array is empty
    2.2 = what if the arthmetic expresion isn't valid 
    2.3 = what is the max length of the array tokens
    2.4 = can it have negtaive integers 
    2.5 = what if the array has just 1 number 
3) Examples - 
    3.1 = Input: tokens = ["1","2","+","3","*","4","-"],Output: 5, 
          Explanation: ((1 + 2) * 3) - 4 = 5
    3.2 = Input: tokens = [],Output: []
          Explanation: empty array
    3.3 = Input: tokens = ["1"],Output: 5
          Explanation: There is only one number, so return 1.
4) Approach = 
    4.1 = Brute Force Approach 
        4.1.1 = iterate through the array, check i
        4.1.2 = if i is integer move, if operator, initialize two int, a = i - 2, b = i - 1
        4.1.3 = if operator is +, add a and b 
        4.1.4 = if i is -, subract a and b 
        4.1.5 = if i is *, multiply a and b 
        4.1.6 = if i is /, divide a and b 
        4.1.7 = After finding one, we create a new list with the result
        Space Complexity = O(n), Time Complexity = O(n^2)
    4.2 = Optimal Approach 
        4.2.1 = iterate through the tokens array 
        4.2.2 = if token is a number, push into stack
        4.2.3 = if token is a operator, pop last two numbers from stack
        4.2.4 = if operator is +, add 
        4.2.5 = if operator is -, subract
        4.2.6 = if operator is *, multiply
        4.2.7 = if operator is /, divide
        4.2.8 = Push the calculated result back onto the stack.
        4.2.9 = Repeat until all tokens are processed.
        4.3.10 = Return the last remaining number in the stack
        Space Complexity = O(n), Time Complexity = O(n)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b) 
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
















