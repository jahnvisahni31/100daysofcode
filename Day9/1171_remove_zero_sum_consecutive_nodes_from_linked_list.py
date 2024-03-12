# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {0: dummy}
        
        while head:
            prefix_sum += head.val
            
            if prefix_sum in prefix_sum_map:
                prev = prefix_sum_map[prefix_sum]
                temp_sum = prefix_sum
                curr = prev.next
                while curr != head:
                    temp_sum += curr.val
                    if temp_sum != prefix_sum:
                        del prefix_sum_map[temp_sum]
                    curr = curr.next
                
                prev.next = head.next
                head = prev
            else:
                prefix_sum_map[prefix_sum] = head

            head = head.next

        return dummy.next
