# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, List1: ListNode | None, List2: ListNode | None) -> ListNode | None:
        dumpy = ListNode(0)
        curr=dumpy
        while List1 and List2:
            if List1.val<=List2.val:
                 curr.next=List1
                 List1=List1.next
            else:
                curr.next=List2
                List2=List2.next
            curr=curr.next
        curr.next=List1 or List2
        return dumpy.next
        
            
        