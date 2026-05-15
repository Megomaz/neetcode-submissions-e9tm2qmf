class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        n = len(nums)

        while r < n:
            if nums[r] == 0:
                nums[r],nums[l] = nums[l],nums[r]
                l +=1 
            r += 1
        r = l
        while r < n:
            if nums[r] == 1:
                nums[r],nums[l] = nums[l],nums[r]
                l +=1 
            r += 1
            
       