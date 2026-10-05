# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        dummy = ListNode(0,head)
        prev = dummy

        for i in range(left - 1):
            prev = prev.next
            cur = cur.next
        
        before = prev
        after = cur

        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        before.next = prev
        after.next = cur
        return dummy.next