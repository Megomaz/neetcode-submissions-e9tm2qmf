class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3
        nums.sort()
        res = []
        count = 0

        for r in range(n):
            if r and nums[r] != nums[r-1]:
                if count > target:
                    res.append(nums[r-1])
                count = 0
            
            count += 1

        if count > target:
            res.append(nums[r])

        return res