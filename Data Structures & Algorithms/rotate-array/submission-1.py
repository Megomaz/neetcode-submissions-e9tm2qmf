class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # reverse all the num in nums
        # extract the first k values and reverse between them (0,k)
        # extrract the last k values and reverse between them (k+1, len(nums))
        n = len(nums)
        k = k % n
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0,n -1)
        reverse(0,k-1)
        reverse(k,n -1)
        