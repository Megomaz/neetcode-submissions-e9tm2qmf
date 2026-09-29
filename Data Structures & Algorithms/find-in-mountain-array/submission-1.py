class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find the index that makes this a valid mountainArr

        l,r = 0, mountainArr.length() - 1
        
        def findPeak(left,right):
            while left < right:
                mid = (left + right) // 2

                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid

            return left
        
        p = findPeak(l,r)
        
        def search(l,r,opp):
            
            while l <= r:
                mid = (l + r) // 2
                mid_val = mountainArr.get(mid)

                if mid_val == target:
                    return mid
                if opp:
                    if mid_val > target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if mid_val < target:
                        r = mid - 1
                    else:
                        l = mid + 1
            
            return -1

        ans = search(0, p, True)
        if ans != -1:
            return ans

        return search(p, r, False)

        
