# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        start = head
        flag = False
        if left == 1:
            flag = True
        for i in range(left-1):
            if i==left-2:
                before = start
            start = start.next
        end = start
        temp = start.next
        start.next = None
        for i in range(right-left):
            prev = end
            end = temp
            temp = temp.next
            end.next = prev
        start.next = temp
        if flag:
            head = end
        else:
            before.next = end
        return head
        

            

        