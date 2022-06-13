from typing import Optional
from ListNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:                
        # if head is None:
        #     return None
        # left = head
        # right = left.next
        # left.next=None

        left = None
        right = head
        while right is not None:                 
            tmp = right.next                        
            right.next = left
            left = right
            right = tmp

        return left
    
head = None
for i in range(5,0,-1):
    head = ListNode(i,head)

head = Solution().reverseList(head)

while head is not None:
    print(head.val)
    head = head.next
        