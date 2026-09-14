class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for row in range(m+1):
            dp[row][0] = 1

        for col in range(n+1):
            dp[0][col] = 1

        for row in range(1,m+1):
            for col in range(1,n+1):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[m-1][n-1]
        
        