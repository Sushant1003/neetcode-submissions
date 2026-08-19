class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, pd, nd = set(), set(), set()
        board = [["."]*n for i in range(n)]
        # each queen is placced in a row
        def dfs(r):
            # if same row or column or diag
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (c in cols) or (r-c in nd) or (r+c in pd):
                    continue
                else:
                    cols.add(c)
                    nd.add(r-c)
                    pd.add(r+c)
                    board[r][c] = "Q"
                    dfs(r+1)
                    cols.remove(c)
                    nd.remove(r-c)
                    pd.remove(r+c)
                    board[r][c] = "."
        dfs(0)
        return res
        