class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,0
        n = len(nums)

        majority = (0,nums[0])

        while r < n:
            if nums[l] != nums[r]:
                l = r
                
            if r - l + 1 > majority[0]:
                majority = (r - l + 1,nums[l])
            r += 1
        return majority[1]