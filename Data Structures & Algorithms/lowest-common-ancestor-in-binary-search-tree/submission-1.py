# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding the problem - 
    Input = root(binary tree), p and q, which are the nodes of that particular binary tree
    Goal = find the lowest common ancestor of those two nodes p and q
    Output = return the node value 
Constraints - Can the root be None 
            - number of nodes in the tree
            - are both p and q guaranteed to exist in the tree
            - can p and q be the same node 
Examples - root = [3,5,1,6,2,0,8,null,null,7,4]
      p = 5, q = 1
      Output = 3

   2. root = [3,5,1,6,2,0,8,null,null,7,4]
      p = 5, q = 4
      Output = 5

   3. root = [1,2]
      p = 1, q = 2
      Output = 1

   4. root = [1,2,3]
      p = 2, q = 3
      Output = 1

   5. root = [1,2,null,3,null,4]
      p = 3, q = 4
      Output = 3
Solution - Solution = DFS (Recursion)
   - First, check if root is None. If yes, return None.
   - Check if root is equal to p or q. If yes, return root.
   - Recursively traverse the left subtree and store
     the result in left.
   - Recursively traverse the right subtree and store
     the result in right.
   - If both left and right are not None, return root,
     as the current node is the LCA.
   - Otherwise, return left or right, whichever is not None.
   - If both are None, return None.

'''
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right
        