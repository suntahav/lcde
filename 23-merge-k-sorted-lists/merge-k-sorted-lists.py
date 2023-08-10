# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, lists):
        length = len(lists)
        if length == 0:
            return None
        elif length == 1: 
            list1 = lists[0]
            list2 = None
        else:
            list1 = lists[0]
            list2 = lists[1]

        if (list1 is None) and (list2 is not None):
            return list2
        if (list2 is None) and (list1 is not None):
            return list1
        if (list1 is None) and (list2 is None):
            return None
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        merged = head
        while (list2 is not None) and (list1 is not None):
            if list1.val < list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        
        if list1 is not None:
            head.next = list1
        if list2 is not None:
            head.next = list2
        return merged

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length > 2:
            div = length // 2
            left = self.mergeKLists(lists[:div])
            right = self.mergeKLists(lists[div:])
            res = self.mergeTwoList([left, right])
        else:
            if len(lists) == 2:
                res = self.mergeTwoList(lists)
            else:
                res = self.mergeTwoList(lists)
        
        return res
