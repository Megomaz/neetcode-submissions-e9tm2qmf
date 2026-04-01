class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search the arr with val x

        # start 2 pointers from that location -> l, r

        # if we chhose left val, incr l and vice versa

        # keep going until we coose k values and return arr[l:r]

        l, r = 0, len(arr) - 1

        # binary search
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

        # now:
        # r = last < x
        # l = first >= x

        left = r
        right = l

        # expand window
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left+1:right]