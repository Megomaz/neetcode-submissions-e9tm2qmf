class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # must eat all bananas in h hours -> worst case we take max from banana pile and eat all 

        left,right = 1, max(piles)

        def helper(rate):
            hours = 0
            for num in piles:
                hours += num // rate if num % rate == 0 else num // rate + 1
            return hours
        
        while left <= right:
            mid = (left + right) // 2

            ans = helper(mid)
            if ans <= h:
                right = mid - 1
            else:
                left = mid + 1

            
        return left