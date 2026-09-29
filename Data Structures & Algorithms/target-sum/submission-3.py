class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i,total):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0

            if (i,total) in cache:
                return cache[(i,total)]
            
            skip = dfs(i+1, total - nums[i])

            add = dfs(i+1, total + nums[i])

            cache[(i,total)] = skip + add
            return skip + add
        return dfs(0,0)