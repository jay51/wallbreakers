# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# problem: loop over 2 linked list and add the corspanding numbers togather and return a new linked list
Time : O(n)
Space: O(n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        current = head
        carry = 0
        """
        This is how you would dynamicly fill a linked list
        head = ListNode(0)
        current = head
        for n in l:
            current.next = ListNode(x)
            current = current.next
        
        return head.next 
        """ 
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum  = carry + x + y
            carry = int(sum / 10)
            current.next = ListNode(sum % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry > 0:
            current.next = ListNode(carry)
        
        return head.next
