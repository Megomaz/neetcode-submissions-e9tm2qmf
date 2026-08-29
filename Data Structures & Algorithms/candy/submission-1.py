class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n

        heap = []

        for idx, val in enumerate(ratings):
            heapq.heappush(heap, (val,idx))

        while heap:
            val, idx = heapq.heappop(heap)

            left = ratings[idx - 1] if idx - 1 >= 0 else float('inf')
            right = ratings[idx + 1] if idx + 1 < n else float('inf')

            if (left < val and right < val):
                l = arr[idx - 1] if idx - 1 >= 0 else 0
                r = arr[idx + 1] if idx + 1 < n else 0
                arr[idx] = max(l, r) + 1
            elif left < val and right >= val:
                l = arr[idx - 1] if idx - 1 >= 0 else 0
                arr[idx] = max(arr[idx],l) + 1
                
            elif right < val and left >= val:
                r = arr[idx + 1] if idx + 1 < n else 0
                arr[idx] = max(arr[idx],r) + 1
             
        print(arr)
        return sum(arr)
        