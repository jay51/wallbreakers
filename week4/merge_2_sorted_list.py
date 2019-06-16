"""
Time : O(n)
Space: O(n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(-1)
        pt = head
        while l1 and l2:
            if l1.val > l2.val:
                pt.next = l2
                l2 = l2.next
                
            else:
                pt.next = l1
                l1 = l1.next
                
            pt = pt.next 
            
        if l1: pt.next = l1
        if l2: pt.next = l2
            
        return head.next
