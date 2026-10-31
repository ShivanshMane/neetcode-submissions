'''
1) Understandng the problem -  
    1.1 - Input - Given sudoko board board 
    1.2 - Goal -  find if its sudoko or not
    1.3 - Output - return true if sudoko else false
2) Constraits - 
    2.1 - what if the board is empty 
    2.2 - what if the board contains only 1 number 
    2.3 - what if the same number appears twice in the row 
    2.4 - what if the same number appears twice in the column
    2.5 - what if the same number appears twice in the 3x3 grid
    2.6 - what if the board has invalid dimensions 
3) Examples - 
    3.1 - Input: board =
        [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
        Output: true
    3.2 - Input: board =
        [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
        Output: false
4) Approach - 
    4.1 - Brute Force Approach 
        4.1.1 - check if . skip it
        4.1.2 - check if number is repating in row 
        4.1.3 - check if the number is repeating in column 
        4.1.4 - check if number is repeating in 3x3 grid 
        4.1.5 - if duplicate if found return false else return true 
        Space Complexity = n, Time Complexity = n^2
    4.2. - Optimal Approach 
        4.2.1 - create sets for row, col, sqaure(3x3 grid)
        4.2.2 - check if . if yes skip 
        4.2.3 - check for board[row][col] with row[r], col[c], sqaure[(r // 3, c // 3)])
        4.2.4 - if any of them exists, return fasle
        4.2.5 - add col, row and sqaure to set 
        4.2.6 - return true 
        Space Complexity = n^2, Time Complexity = n^2
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue
                
                if (num in rows[r]
                    or num in cols[c]
                    or num in squares[(r //3, c //3)]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
                
        return True



















        