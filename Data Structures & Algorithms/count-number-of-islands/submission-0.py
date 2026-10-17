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
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
        