'''
Understanding the problem = 
    Input - 2D grid, where 1 represents land 0 represents water
    Goal - count the number of islands in the given 2D grid 
    Output - return the count( no of islands)
Constraints - can the grid be empty  
            - can it contain only islands or only water 
            - what is the max length of dimensions of the grid 
            - are islands connected diagonally as well
            - can the gird only contain 1 and 0 
Examples = Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]], Output: 1
        = Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]], Output: 4
    = Input: grid = [
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"],
    ["0","0","0","0","0"]], Output: 0
    Input: grid = [
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"]], Output: 1
Solution = 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        
        ROWS, COLS = len(grid), len(grid[0])
        countIslands = 0 

        def dfs( r,c):
            #this is the base case 1( checks the boundary)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 
    
            if grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"

            dfs( r - 1, c) #Up 
            dfs( r + 1, c) #Down 
            dfs( r, c - 1) #Left
            dfs( r, c + 1) #Right 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    countIslands += 1
                    dfs(r,c)
        return countIslands
            















    