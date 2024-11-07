# Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # Initialize dictionaries to store sets of seen digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Traverse each cell in the board
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                # Skip empty cells
                if num == '.':
                    continue
                
                # Check the row
                if num in rows[r]:
                    return False
                rows[r].add(num)
                
                # Check the column
                if num in cols[c]:
                    return False
                cols[c].add(num)
                
                # Check the 3x3 box
                box_index = (r // 3) * 3 + (c // 3)
                print(box_index)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        # If no violations are found, the board is valid
        return True
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

x = Solution()
print(x.isValidSudoku(board))