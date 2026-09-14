class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def backtrack(row,col):
            if row == m - 1 and col == n - 1 :
                return 1

            if (row,col) in dp:
                return dp[(row,col)]

            if not 0 <= row < m or not 0 <= col < n:
                return 0

            down = backtrack(row + 1, col)
            right = backtrack(row, col + 1)

            dp[(row,col)] = down + right
            return dp[(row,col)]
        
        return backtrack(0,0)
        