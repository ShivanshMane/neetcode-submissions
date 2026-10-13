# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding the problem- 
    Input = We are given a root of binary tree
    Goal = find out if thats actually a binary tree
         = left subtree of every node contains only nodes with keys less than the nodes key 
         = right subtree of every node contains only nodes with keys more than the nodeskey
         = both left and right are also binary tree
    Output = return True if binary tree else False
Constraints - what if root is None
            - can it have negative values
            - range of node, min, max
            - skewed binary tree 
            - Duplicates allowed 
Examples - Input: root = [2,1,3], Output: true
         - Input: root = [1,2,3], Output: false
Solution = DFS (Recursion)
   - We'll use DFS to traverse the binary tree.
   - Maintain a minimum and maximum allowed value
     for each node.
   - Initially, the minimum is negative infinity
     and the maximum is positive infinity.
   - If a node is None, return True.
   - If the current node's value is outside the
     allowed range, return False.
   - Recursively check the left subtree with the
     current node's value as the new maximum.
   - Recursively check the right subtree with the
     current node's value as the new minimum.
   - Return True only if both subtrees are valid.
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
        
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
        return valid(root, float("-inf"), float("inf"))














        