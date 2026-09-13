class MyHashSet:

    def __init__(self):
       self.buckets = [[] for _ in range(10000)] 

    def add(self, key: int) -> None:
        k = key % 10000
        if key in self.buckets[k]:
            return
        self.buckets[k].append(key)

    def remove(self, key: int) -> None:
        k = key % 10000
        if key in self.buckets[k]:
            self.buckets[k].remove(key)

    def contains(self, key: int) -> bool:
        k = key % 10000
        return key in self.buckets[k]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)