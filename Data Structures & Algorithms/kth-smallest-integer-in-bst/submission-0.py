# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding the problem - Its a binary search tree
    Input = the root of binary tree, and an integer k
    Goal = find the kth smallest value in the tree
    Output = return the kth smallest value in the tree
Constraints = what if the root is None
            = Duplicates(if binary search tree this dosen't apply)
            = min, max length of the binary tree(basically the nodes)
Examples = Input: root = [2,1,3], k = 1, Output: 1
         = Input: root = [4,3,5,2,null], k = 4, Output: 5
Solution =  Use iterative DFS with a stack.
         - Since it is a BST, inorder traversal (Left -> Node -> Right)
      visits nodes in ascending order.
         - Initialize an empty stack and curr = root.
         - Run a while loop while curr or stack is not empty.
         - Keep moving left and push each node onto the stack.
         - Once curr becomes None, pop the top node from the stack.
         - Decrease k by 1 because we visited the next smallest node.
         - If k == 0, return curr.val.
         - Otherwise, move to the right subtree using curr = curr.right.
         - Repeat until we find the kth smallest element.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            k -= 1
            if k == 0 :
                return curr.val
            curr = curr.right













        