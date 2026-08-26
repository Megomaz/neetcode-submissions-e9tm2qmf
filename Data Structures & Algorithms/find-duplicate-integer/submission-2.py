class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow , fast = 0,0
        
        while True:
            slow,fast = nums[slow], nums[nums[fast]]

            if slow == fast:
                break

        print((slow,fast))
        new_slow = 0  

        while True:
            new_slow, fast = nums[new_slow],nums[fast]
            if new_slow == fast:
                return new_slow
            
        return -1
       