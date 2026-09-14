class Solution:
    def rob(self, nums: List[int]) -> int:
        # last index and start cant be used in the same run
        dp = {}
        # start, end -> start + 1, end - 1
        end = len(nums)
        if end == 1:
            return nums[0]
        def backtrack(i,end):
            if i >= end:
                return 0

            if (i,end) in dp:
                return dp[(i,end)]

            take = nums[i] + backtrack(i + 2,end)
            skip = backtrack(i+1,end)

            dp[(i,end)] = max(take,skip)
            return dp[(i,end)]
        
        return max(backtrack(0, end - 1), backtrack(1,end))