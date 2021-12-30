# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
                
        cursor = dummy
        delayedCursor = dummy
        
        while cursor.next and n > 0:
            cursor=cursor.next
            n-=1

        while cursor.next:
            cursor=cursor.next
            delayedCursor=delayedCursor.next
            
        delayedCursor.next=delayedCursor.next.next            
        return dummy.next