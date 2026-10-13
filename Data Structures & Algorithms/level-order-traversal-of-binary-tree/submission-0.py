# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding the problem - 
    Input = Given a binary tree
    Goal = traverse the binary tree and make nested lists of its nodes, such that each     sublist contains the values of its node at that particular level
    Output = Return the nestes list where each sublist is its node at that particular level
Constraints - what if root is none
            - max no of nodes
            - skewed binary list 
            - can nodes be positive or negative
            - only one node that
Examples - Input: root = [1,2,3,4,5,6,7], Output: [[1],[2,3],[4,5,6,7]]
          Input: root = [1], Output: [[1]]
          Input: root = [], Output: []
Solution = BFS (Queue)
    - First, check if root is None. If yes, return [].
    - Initialize an empty result list (res).
    - Initialize a queue and add the root node.
    - While the queue is not empty, traverse the tree.
    - Find the number of nodes at the current level.
    - Create an empty list to store the current level's values.
    - For each node at the current level:
        - Remove the node from the queue.
        - Add its value to the current level list.
        - If the left child exists, add it to the queue.
        - If the right child exists, add it to the queue.
    - Add the current level list to res.
    - Return res after all levels are processed.
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        
        q = deque([root])
        while q: 
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        return res































        