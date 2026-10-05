class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        for count, var in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count == 0:
                continue
            heapq.heappush(max_heap, (count, var))
        
        string = ''
        hold = None

        while max_heap or hold:
            if hold:
                if hold[1] != string[-1]:
                    heapq.heappush(max_heap, hold)
                    hold = None
                    continue
                elif not max_heap and string[-1] == hold[-1] == string[-2]:
                    break

            count, var = heapq.heappop(max_heap)

            

            if len(string) >= 2 and string[-1] == var == string[-2]:
                hold = (count, var)
                continue

            string += var

            if count + 1 < 0:
                heapq.heappush(max_heap, (count + 1, var))

                
        return string
        # greedy, need to see if the last 2 werent the same one we get from when we pop 