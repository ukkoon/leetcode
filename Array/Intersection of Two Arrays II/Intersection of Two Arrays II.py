from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        cursor1 = 0
        cursor2 = 0

        result = []
        
        while cursor1 < len(nums1) and cursor2 < len(nums2):
            if nums1[cursor1] == nums2[cursor2]:            
                result.append(nums1[cursor1])
                cursor1+=1
                cursor2+=1
            elif nums1[cursor1] > nums2[cursor2]:
                cursor2+=1
            else:
                cursor1+=1
                
        return result            
