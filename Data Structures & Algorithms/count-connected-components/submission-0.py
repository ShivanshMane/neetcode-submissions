'''
Understanding the problem = 
    Input = n nodes, and array list, pair nodes
    Goal = find out the connected components in the undirected graph 
    Output = return the connected components in the graph, connected
Constraints = what if n is 0 
            = what is max length of nodes
            = can it have negative values 
            = can it duplicate values or nodes
Examples = Input: n = 5, edges = [[0,1],[1,2],[3,4]], Output: 2
         = Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]], Output: 1
         = Input: n = 1, edges = [[]], Output: 1
Approach = Build an adjacency list, just like Graph Valid Tree.
         = Create a visit HashSet.
         = Loop through every node from 0 to n - 1.
         = Whenever we find a node that hasn't been visited, increase our component count by 1 and use DFS to visit all nodes connected to it.
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        count = 0 
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        return count


        