from typing import Optional
from ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        cursor = result
        while list1 or list2:            
            if list1 and list2:
                if list1.val>=list2.val:
                    result.next = list2
                    result = result.next
                    list2=list2.next
                else :
                    result.next=list1
                    result = result.next
                    list1=list1.next
                continue

            if list1 is None:
                result.next=list2
                result = result.next
                list2=list2.next
                continue

            if list2 is None:
                result.next=list1
                result = result.next
                list1=list1.next
                continue

        return cursor.next
                
        
head1=ListNode(1,ListNode(2,ListNode(4)))    
head2=ListNode(0)    
head3 = Solution().mergeTwoLists(None,head2)

while head3 is not None:
    print(head3.val)
    head3 = head3.next
        