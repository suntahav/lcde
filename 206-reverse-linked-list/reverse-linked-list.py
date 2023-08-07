# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        fp = head
        sp = head.next
        temp = None
        while sp is not None:
            fp.next = temp
            temp = fp
            fp = sp
            sp = sp.next
        fp.next = temp
        return fp
