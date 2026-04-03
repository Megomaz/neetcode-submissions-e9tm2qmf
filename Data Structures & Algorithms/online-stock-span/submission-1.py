class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        count = 1
        for i in range(len(self.arr) -1, -1,-1):
            if self.arr[i][0] <= price:
                count += self.arr[i][1]
                self.arr.pop()
            else:
                break

        self.arr.append((price,count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)