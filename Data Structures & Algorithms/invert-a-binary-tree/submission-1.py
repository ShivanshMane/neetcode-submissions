# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1) Understanding = 
   Input = Binary tree root 
   Goal = Invert the binary tree, means inverting the nodes in the tree
   Output = Return the node of the inverted binary tree
2) Constraints = what if root is None, 
                 Can the tree contain only one node, 
                 can the tree contain duplicate values,
                 can nodes be negative or zero, 
                 max number of nodes
3) Examples = Input: root = [1,2,3,4,5,6,7], Output: [1,3,2,7,6,5,4]
              Input: root = [3,2,1], Output: [3,1,2]
              Input: root = [], Output: []
4) Solution = We can use DFS(dfs is an algorithm which help us to traverse through the tree as deep as possible, one side then other, for example, we'll dive deep in the left side first and then come to the upper level and then dive on the right side)
            = We can call the dfs algorithm recursively such that each nodes get swapped
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None 
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        