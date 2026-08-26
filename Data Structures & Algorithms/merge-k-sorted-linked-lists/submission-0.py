# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        min_heap = []
        i = 0

        for c in lists:
            if c:
                heapq.heappush(min_heap,(c.val,i))
            i += 1
            
        while min_heap:
            val, idx = heapq.heappop(min_heap)

            cur.next = lists[idx] 
            cur = cur.next

            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(min_heap,(lists[idx].val,idx))
                

        return dummy.next