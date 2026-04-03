class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}

        def dfs(i):
            if i == len(s):
                return 0

            if (i) in dp:
                return dp[(i)]

            res = 1 + dfs(i+1)

            for word in dictionary:
                if s.startswith(word, i): # (prefix,start)
                    res = min(res,dfs(i + len(word)))
            
            dp[i] = res
            return res

        return dfs(0)