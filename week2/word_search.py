
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # loop over each char and do dfs from that position
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word):
                    return True
        return False
        
        
    def dfs(self, board, row, col, word):
        if len(word) == 0: return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        # if we walk to this char and it's not equal to char we're looking for 
        if word[0] != board[row][col]:
            return False
        
        # to make sure not to modify the board
        visited = board[row][col]
        # mark visited chars 
        # empty strings are falsey
        board[row][col] = ""
        
        # walk from the current char not including the current char
        result =self.dfs(board, row + 1, col, word[1:]) or \
                self.dfs(board, row - 1, col, word[1:]) or \
                self.dfs(board, row, col + 1, word[1:]) or \
                self.dfs(board, row, col - 1, word[1:])
        
        # backtracking/unchanging chars in the board
        board[row][col] = visited
        
        return result
        
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# Test: True
word = "ABCCED"



