# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revList(self, head):
        fp = head
        if fp is None:
            return fp
        temp = None
        sp = head.next
        while sp is not None:
            fp.next = temp
            temp = fp
            fp = sp
            sp = sp.next
        fp.next = temp
        return fp

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        num_nodes = 0
        temp = head
        while temp is not None:
            num_nodes += 1
            temp = temp.next
        if num_nodes == 0:
            return head
        else:
            nodes_for_sp = num_nodes // 2 

        fp = head
        sp = head
        while nodes_for_sp - 1 > 0:
            nodes_for_sp -= 1
            sp = sp.next
        temp = sp
        sp = sp.next
        temp.next = None
        sp = self.revList(sp)
        while sp is not None:
            if fp.next is None:
                fp.next = sp
                break
            temp = sp
            sp = sp.next
            temp.next = fp.next
            fp.next = temp
            fp = fp.next.next