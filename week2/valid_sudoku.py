class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_numbers = []
            col_numbers = []
            box_grids = []
            for j in range(9):
                row_n = board[row][j]
                col_n = board[j][row]

                if col_n != ".": 
                    if col_n in col_numbers:
                        return False
                    col_numbers.append(col_n)

                if row_n != ".":
                    if row_n in row_numbers:
                        return False
                    row_numbers.append(row_n)

                row_index = 3*(row//3)
                col_index = 3*(row%3)
                cell = board[row_index+j//3][col_index+j%3] 
                if cell != ".":
                    if cell in box_grids:
                        return False
                    box_grids.append(cell)
            
        return True

# Test

# True
something = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]


# False
something1 =  [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

# False
something2 = [
["7",".",".",".","4",".",".",".","."],
[".",".",".","8","6","5",".",".","."],
[".","1",".","2",".",".",".",".","."],
[".",".",".",".",".","9",".",".","."],
[".",".",".",".","5",".","5",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".","2",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]]

# False
something3 = [
    [".", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["1", ".", ".", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", ".", "2", ".", "6", ".", "."],
    [".", "9", ".", ".", ".", ".", ".", "7", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["8", ".", ".", "8", ".", ".", ".", ".", "."]
]

print(fn(something))
