class Solution:
    def numDecodings(self, s: str) -> int:
        # take 1 number or take 2
        # must be valid e.g. if 2 -> then 2nd must be <= 6
        # if 1, cant be a '0'

        dp = {}

        def backtrack(i):
            if i >= len(s):
                return 1
            
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0

            one_letter = backtrack(i+1)
            two_letter = 0

            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                two_letter = backtrack(i+2)

            dp[i] = one_letter + two_letter
            return dp[i]

        return backtrack(0)