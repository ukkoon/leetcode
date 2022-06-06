from typing import Optional
from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        fast = dummy
        slow = dummy
        
        for i in range(n+1):
            fast = fast.next  

        while fast is not None:            
            slow = slow.next                        
            fast = fast.next
                
        slow.next=slow.next.next                   
        
        return dummy.next

head = None
for i in range(10,0,-1):
    head = ListNode(i,head)

head = Solution().removeNthFromEnd(head,10)

while head is not None:
    print(head.val)
    head = head.next
        