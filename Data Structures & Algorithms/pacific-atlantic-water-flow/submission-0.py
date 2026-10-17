class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # Sets to track cells that can reach each ocean
        pacific = set()
        atlantic = set()

        # DFS helper function
        def dfs(r, c, visited):

            # If already visited, return
            if (r, c) in visited:
                return

            # Mark current cell as visited
            visited.add((r, c))

            # Four directions: down, up, right, left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                newRow = r + dr
                newCol = c + dc

                # Check if neighbor is inside the grid
                if 0 <= newRow < ROWS and 0 <= newCol < COLS:

                    # Reverse DFS: move to equal or higher height
                    if heights[newRow][newCol] >= heights[r][c]:
                        dfs(newRow, newCol, visited)

        # Start DFS from top and bottom rows
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        # Start DFS from left and right columns
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)

        # Find cells that can reach both oceans
        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result