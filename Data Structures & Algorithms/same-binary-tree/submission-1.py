# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1) Understading the problem = 
   Input = two roots of a binary tree, p and q 
   Goal = we need to check if these trees are equivalent
   Output = return true if equivalent or false if not 
2) Constraints = can p and q be empty
                 can there be only one side of the trees
                 can p be empty when q is not or vice e versa
                 whats the max number of nodes
3) Examples = p = [1,2,3], q = [1,2,3]
            = p = [4,7], q = [4,null,7]
            = p = [1,2,3], q = [1,3,2]
            = p = [], q = [1,2,3]
            = p = [], q = []
4) Solution = DFS (Recursion)
   - Use DFS to compare both trees node by node.
   - If both nodes are None, return True.
   - If one node is None and the other isn't, return False.
   - If the values of the current nodes are different,
     return False.
   - If the values match, recursively compare the left
     subtrees and the right subtrees.
   - Return True only if both recursive comparisons
     return True.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
         return True 
      
      if not p or not q:
         return False
      
      if p.val != q.val:
         return False
      
      return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
        