# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        while fp is not None:
            if fp.val == 100001:
                return True
            else:
                fp.val = 100001
                fp = fp.next
        
        return False