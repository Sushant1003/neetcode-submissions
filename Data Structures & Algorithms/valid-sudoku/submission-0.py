class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] != '.':
                    s.add(board[i][j])
        # column
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i] != '.':
                    s.add(board[j][i])
        # box
        for startr,startc in [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]:
            s = set()
            for row in range(startr, startr+3):
                for col in range(startc,startc+3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col] != '.':
                        s.add(board[row][col])
        return True
        