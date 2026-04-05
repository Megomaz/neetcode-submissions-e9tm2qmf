class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)

        def canShip(cap):
            total_weight = 0
            ships = 0
            for w in weights:
                total_weight += w
                if total_weight > cap:
                    ships += 1
                    total_weight = w
            return ships < days
            
                
        while l <= r:
            mid = (l+r) // 2

            if canShip(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l