# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        # while fp is not None:
        #     if fp.val == 100001:
        #         return True
        #     else:
        #         fp.val = 100001
        #         fp = fp.next

        # floyd cycle detection
        sp = head
        if fp == None:
            return False
        while (fp is not None) and (fp.next is not None):
            fp = fp.next.next
            sp = sp.next

            if fp == sp:
                return True
        
        return False