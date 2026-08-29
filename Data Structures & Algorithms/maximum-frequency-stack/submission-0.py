class FreqStack:

    def __init__(self):
        self.heap = []
        self.freq = {}
        self.idx = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val,0) + 1
        freq = self.freq[val]

        heapq.heappush(self.heap, (-freq,-self.idx,val))
        self.idx += 1

    def pop(self) -> int:
        freq, idx, val = heapq.heappop(self.heap)
        self.idx = len(self.heap)
        self.freq[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()