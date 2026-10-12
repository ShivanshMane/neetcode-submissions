# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1) Understanding the problem = 
   Input = root of a binary tree
   Goal = find the maximum length of the binary tree
   Output = return the depth of the binary tree(basically length)
2) Constraints = can the root be None
                 can there only be one side of the tree 
                 number of nodes of the tree
                 Node val min, max value
3) Examples = Input: root = [1,2,3,null,null,4], Output: 3
            = Input: root = [], Output: 0
4) Solution = We can use the dfs(where we traverse through the entire tree one side at a time, and going as deep as possible), using dfs and then calculcating the length of that node and storing it, then traversing the other side and storing and then returning teh max        
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
    
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)    