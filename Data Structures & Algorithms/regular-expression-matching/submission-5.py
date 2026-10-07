class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i,j):
            if j >= len(p):
                return i == len(s)
            
            if (i,j) in memo:
                return memo[(i,j)]
            match = i < len(s) and (p[j] == '.' or s[i] == p[j])

            
            if j + 1 < len(p) and p[j+1] == '*':
               v = match and dfs(i+1, j) or  dfs(i, j+2)
            else:
                v = match and dfs(i+1, j+1)
            
            memo[(i,j)] = v
            return v
        
        return dfs(0,0)
