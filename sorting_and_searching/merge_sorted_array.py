# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = m+n-1
        cursor1 = m-1
        cursor2 = n-1
        
        while cursor1 >=0 and cursor2 >=0 :                         
            if nums1[cursor1] < nums2[cursor2]:
                nums1[i] = nums2[cursor2]
                cursor2-=1
            else:
                nums1[i] = nums1[cursor1]
                cursor1-=1            
            i-=1

        if cursor2>=0:
            nums1[:i+1] = nums2[:cursor2+1]        