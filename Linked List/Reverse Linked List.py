# Definition for singly-linked list.
from math import factorial
from subprocess import call
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Iteratively Ugly Solution #
# First idiot trying #
        
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return head
#         dummy = ListNode(999,head)
#         head=dummy        

#         temp = head.next.next
#         head.next.next = head
        
#         while temp is not None:                          
#             new_temp = temp.next
#             temp.next=head        
#             head = temp            
#             temp = new_temp        
        
#         dummy.val=dummy.next.val
#         dummy.next=None
#         return head

# Iteratively Pretty Solution #
# Trying by reference #

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         before = None        
        
#         while head is not None:                          
#             after = head.next
#             head.next=before
#             before = head
#             head = after

#         return before


# Recursively Solution #
# First trying#

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = self.rec(head,None)                 
        return result[1]

    def rec(self,head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            cursor = head
            return head, cursor

        else :                            
            caller = head
            callee = self.rec(head.next,None)    
            callee.next=caller

            caller.next=None
            return caller, cursor

# Recursively solution #
# reference code #

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next=None
        return newHead

# class Rec:
#     def factorial(self, n)->int:
#         if n == 1:
#             return n
#         else :
#             return n * self.factorial(n-1)