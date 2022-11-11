from typing import Optional
from lib.ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor1 = ListNode(-1,list1)
        cursor2 = ListNode(-1,list2)
        
        while list1:
            print(list1.val)
            list1=list1.next
        
        while list2:
            print(list2.val)
            list2=list2.next

        return

list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))


Solution().mergeTwoLists(list1,list2)