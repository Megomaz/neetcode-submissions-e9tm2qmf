class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        q = deque()
        q.append('0000')
        time = 0

        while q:
            size = len(q)
            
            for _ in range(size):
                lock = q.popleft()

                if lock in deadends:
                    continue
                
                if lock == target:
                    return time

                
                deadends.add(lock)
                
                for i in range(4):
                    val = int(lock[i])
                    up = '0' if val + 1 >= 10 else str(val + 1)
                    down = '9' if val - 1 <= -1 else str(val - 1)

                    new_up = lock[:i] + up + lock[i+1:]
                    if new_up not in deadends:
                        q.append(new_up)

                    new_down = lock[:i] + down + lock[i+1:]
                    if new_down not in deadends:
                        q.append(new_down)
                    

            time += 1


        return -1
