# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Understanding the problem -
    Input = Two binary trees, i.e root and SubRoot
    Goal = check if the SubRoot is a subtree of root
    Output = True or False 
Constraints - can root and SubRoot both be None 
            - can root be None and SubRoot be normal binary tree
            - what if length of SubRoot is greater than length of root
Examples - root = [1,2,3,4,5], subRoot = [2,4,5]
         - root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
         - root = [], subRoot = []
         - root = [], subRoot = [1,2,3,]
         - root = [1,2,3], subRoot = [12,3,4,5,6,7,8]
Solution - We will use the dfs algorithm and first check if not root and not subroot, return True, then find if any node of root is equal to the node of subRoot, then we can ppply dfs and check root.left and subRoot.left and root.right and subRoot.right 
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: 
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))

        