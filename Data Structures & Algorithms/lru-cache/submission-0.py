class Node:
    def __init__(self, val, key,nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def remove(self,node) -> int:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    
    def insert(self,node) -> None:
        node.prev = self.tail.prev
        node.nxt = self.tail
        self.tail.prev.nxt = node
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        node = Node(value,key)
        self.insert(node)
        self.size -= 1

        if self.size < 0:
            del self.hashmap[self.head.nxt.key]
            self.remove(self.head.nxt)
            self.size += 1
        
        self.hashmap[key] = node
        
        