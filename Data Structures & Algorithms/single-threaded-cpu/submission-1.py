class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[i,times[1],times[0]] for i, times in enumerate(tasks)]
        # idx, process,enque 
        tasks.sort(key=lambda x:(x[2],x[1]))
        heap = []
        res = []
        l = 0
        time = 0
        
        while l < len(tasks) or heap:

            if heap:
                pt, idx, et = heapq.heappop(heap)
                res.append(idx)
                time = max(time + pt, et + pt)

                while l < len(tasks) and time >= tasks[l][2]:
                    heapq.heappush(heap,(tasks[l][1],tasks[l][0],tasks[l][2]) )
                    l += 1
            else:
                heapq.heappush(heap,(tasks[l][1],tasks[l][0],tasks[l][2]))      
                l += 1
            
            
        return res   


        