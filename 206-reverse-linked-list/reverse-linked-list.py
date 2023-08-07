# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        last_node = head
        
        reversed_list = self.reverseList(head.next)
        if reversed_list is None:
            return last_node
        else:
            temp = reversed_list
            while temp.next is not None:
                temp = temp.next
            temp.next = last_node
            last_node.next = None
        return reversed_list
