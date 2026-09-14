class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def backtrack(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]
                
            res = 0
            skip = backtrack(i + 1)
            take = nums[i] + backtrack(i + 2)
            dp[i] = max(skip, take)

            return dp[i]
        
        return backtrack(0)