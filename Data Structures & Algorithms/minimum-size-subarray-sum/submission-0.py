class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # loop thorugh arr keeping track of total sum
        l = 0
        size = float('inf')
        total = 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                size = min(size, r - l + 1)
                total -= nums[l]
                l += 1

        return size if size != float('inf') else 0
