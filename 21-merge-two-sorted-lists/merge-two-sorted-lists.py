# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        if (list1 is not None) and (list2 is not None):
            if list1.val > list2.val:
                start = list2
                list2 = list2.next
            else:
                start = list1
                list1 = list1.next
        elif list1 is not None:
            start = list1
            list1 = list1.next
        elif list2 is not None:
            start = list2
            list2 = list2.next
        else:
            return None
        temp = start
        while (list1 is not None) or (list2 is not None):
            if list1 is None:
                temp.next = list2
                break
            elif list2 is None:
                temp.next = list1
                break
            else:
                if list1.val > list2.val:
                    temp.next = list2
                    list2 = list2.next
                else:
                    temp.next = list1
                    list1 = list1.next
            temp = temp.next
        return start
            
            