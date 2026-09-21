class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap with lowest room number
        rooms = [0] * n
        # heap with meetings start/end?
        meetings.sort()
        # return max of dp?
        i = 0
        end_heap = [] # end,room
        rooms_used = [i for i in range(n)]

        for i in range(len(meetings)):
            start,end = meetings[i] #end,room

            while end_heap and start >= end_heap[0][0]:
                e, room = heapq.heappop(end_heap)
                heapq.heappush(rooms_used, room)

            if len(end_heap) == n:
                e, room = heapq.heappop(end_heap)
                heapq.heappush(rooms_used, room)
                end = e + (end - start)
           
                
            available = heapq.heappop(rooms_used)
            rooms[available] += 1
            heapq.heappush(end_heap,(end ,available))
            


        ans = -float('inf')
        for idx,val in enumerate(rooms):
            if val > ans:
                ans = val
                i = idx
        return i

        
        

        


        
