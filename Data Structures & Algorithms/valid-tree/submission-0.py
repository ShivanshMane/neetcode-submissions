'''
Understanding the problem - 
    Input = n, the nodes from 0 to n - 1, list of undirected edges(each list is pair)
    Goal = is to check if the list of nodes make a valid tree
    Output = we need to rteurn bool which is true or false after checking if tree is valid
Constraints = what if nodes is 0 or 1 
            = what is max length of nodes
            = can it have negative values 
            = can it duplicate values or nodes
Examples = Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]], Output: true
         = Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]], Output: false
         = Input: n = 1, edges = [[]], Output: true
         = Input: n = 2, edges = [[0,1]], Output: true 
Approach = Optimal approach 
         = use a dfs here to traverse through the tree and check if its a vlaid one
         = first we'll create and adj list which has all the nodes, and its neighbor 
         = we append n1 and n2, and n2 and n1, i mean it goes both ways 
         = create a hashset call visit, which keeps track of the nodes we have visited
         = then dfs function, which checks if node in visit, return false, and then add
         = then for loop to check neighbors, if neighbor is parent, continue
         = and call dfs with neighbor and node, if not dfs return false 
         = else return true 
         = return dfs(0, -1) and len(visit) == n ( this checks both requirements)
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
                
            return True
        return dfs(0, -1) and len(visit) == n
        