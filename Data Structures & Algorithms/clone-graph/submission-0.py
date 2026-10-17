"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
Understanding the problem -
    Input = We are given a node in a connected graph
    Goal = create a clone, basically a copy of the graph, not original nodes but a copy 
    Output = return a clone of the connected graph(connections should remain same)
Constraints = what if theres just one node
            = what if node is null or empty 
            = what is the max length of the graph 
Examples = Input: adjList = [[2],[1,3],[2]], Output: [[2],[1,3],[2]]
         = Input: adjList = [[]], Output: [[]]
         = Input: adjList = [], Output: []
Solution = so we will use dfs along with recursion and use hashmap to store the cloned nodes as the value and the original node as the key, just to make sure and check if we have visited that node. 
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #empty hashmap
        oldToNew = {}
        def dfs(node):
            # check if node exists in oldToNew
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a new copy of the current node
            copy = Node(node.val)

            # Store original node -> cloned node
            oldToNew[node] = copy

            # Recursively clone all neighbors
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
            
            # return the copy of node
            return copy
        
        # handles empty graph 
        if not node:
            return None
        
        # start dfs again 
        return dfs(node)











        