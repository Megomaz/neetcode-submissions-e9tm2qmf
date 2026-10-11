class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        res = (len(nums) +1) // 2
        count = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                count = 1
                continue
            
            count += 1
            if count >= res:
                return nums[r]
        return nums[0]
