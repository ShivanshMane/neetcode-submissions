'''
Understand the problem = 
    Input = 2-D grid of characters board, string word
    Goal = find the word in the board(2-D grid)
    Output = return True if the word is found else false
Constraints = length of the word
            = can the grid be empty 
            = is board and word both lowercase or uppercase or mix 
            = can it have any numbers(int)
Examples = Input:  board = [
                         ["A","B","C","D"],
                         ["S","A","A","T"],
                         ["A","C","A","E"]
                         ],
                    word = "BAT", Output: false
Solution = we can use dfs algorithm to traverse in the grid, and we'll use recursion along with it and backtracking to backtrack the letters    

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r>=ROWS or c >= COLS or word[i] != board[r][c] or (r,c)  in path):
                return False

            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or 
                  dfs(r - 1, c, i + 1) or 
                  dfs(r, c + 1 , i + 1) or 
                  dfs(r, c - 1, i + 1)) 
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True 
        return False
    













