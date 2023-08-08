# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = head
        sp = head
        while n > 0:
            n -= 1
            sp = sp.next
        if sp is None:
            if fp is not None:
                return head.next
            else:
                return fp
        
        while sp.next is not None:
            sp = sp.next
            fp = fp.next
        
        fp.next = fp.next.next
        return head