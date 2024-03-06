# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        sl = head
        nv = head.next
        while sl != nv:
            if not nv or not nv.next:
                return False
            sl = sl.next
            nv = nv.next.next
        return True
