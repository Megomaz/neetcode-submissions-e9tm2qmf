class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        rows = set()
        posDiag = set()
        negDiag = set()

        def backtrack(cols):
            if cols == n:
                self.res += 1
                return
            

            for row in range(n):
                if row in rows or row - cols in negDiag or row + cols in posDiag:
                    continue
                
                rows.add(row)
                posDiag.add(row + cols)
                negDiag.add(row - cols)

                backtrack(cols + 1)

                rows.remove(row)
                posDiag.remove(row + cols)
                negDiag.remove(row - cols)
        backtrack(0)
        return self.res