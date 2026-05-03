class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        n = len(nums)
        def dfs(total):
            if total > target:
                return 0
            
            if total == target:
                return 1
            
            if total in cache:
                return cache[total]

            count = 0
            for i in range(n):
                count += dfs(total + nums[i])
            
            cache[total] = count
            return count

        return dfs(0)