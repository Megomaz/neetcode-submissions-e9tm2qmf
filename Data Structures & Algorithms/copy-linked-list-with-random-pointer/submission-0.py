"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original = {None: None}

        cur = head
        # A, B, C
        # A', B', C'
        # A -> A', B -> B', C -> C'

        while cur:
            new_copy = Node(cur.val)
            original[cur] = new_copy
            cur = cur.next
        
        cur = head

        while cur:
            new_copy = original[cur]
            new_copy.next = original[cur.next]
            new_copy.random = original[cur.random]

            
            cur = cur.next

        return original[head]