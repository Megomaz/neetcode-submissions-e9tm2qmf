class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def bananaPerHour(mid):
            hour = 0

            for b in piles:
                hour += (b // mid) + 1 if (b % mid) != 0 else b // mid
                if hour > h:
                    return False

            return True

        while l <= r:
            mid = (l + r) // 2

            if bananaPerHour(mid):
                r = mid - 1
            else:
                l = mid + 1
        

        return l

        

