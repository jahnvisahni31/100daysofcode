# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first_ptr = dummy
        second_ptr = dummy

        # Move the first pointer n+1 steps forward
        for i in range(n + 1):
            first_ptr = first_ptr.next

        # Move both pointers together until the first pointer reaches the end
        while first_ptr is not None:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        # Remove the nth node
        second_ptr.next = second_ptr.next.next

        return dummy.next
