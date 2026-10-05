class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        rows,pDiagonal,nDiagonal = set(), set(), set()

        def backtrack(col):
            if col == n:
                val = [''.join(row) for row in board]
                res.append(val)
                return 
            
            for row in range(n):
                pD = row + col 
                pN = row - col 

                if row in rows or pD in pDiagonal or pN in nDiagonal:
                    continue
                
                rows.add(row)
                pDiagonal.add(pD)
                nDiagonal.add(pN)
                board[row][col] = 'Q'

                if backtrack(col + 1):
                    return 

                board[row][col] = '.'
                rows.remove(row)
                pDiagonal.remove(pD)
                nDiagonal.remove(pN)

            return False
        backtrack(0)
        return res
    
                