# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        odd = head
        even =  head.next
        even_head = even # first even Node
        
        # check even because the last node is going be even node
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        odd.next = even_head
        return head
            
