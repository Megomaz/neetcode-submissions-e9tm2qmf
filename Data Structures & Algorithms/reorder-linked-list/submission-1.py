# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        prev = None
        slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        
        cur = head
        second = prev


        while second:
            temp = cur.next
            temp2 = second.next

            cur.next = second
            second.next = temp

            cur = temp
            second = temp2
        
