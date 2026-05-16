import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        char_count = Counter(s)
        ans = []
        temp = None

        for key,val in char_count.items():
            heapq.heappush(heap,(-val,key))
        
        while heap or temp:    
            if temp and not heap:
                return ''

            val, char = heapq.heappop(heap)

            ans.append(char)

            if temp:
                heapq.heappush(heap,(temp[0], temp[1]))
                temp = None

            if val + 1 < 0:
                temp = (val + 1,char)
            
        
        return ''.join(ans)