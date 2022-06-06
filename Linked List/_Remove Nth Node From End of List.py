# Definition for singly-linked list.
from typing import Optional
from ListNode import ListNode

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

nodes = ListNode(val=1,next=ListNode(val=2,next=ListNode(val=3,next=ListNode(val=4,next=ListNode(val=5)))))
solution = Solution()
result = solution.removeNthFromEnd(head=nodes,n=2)