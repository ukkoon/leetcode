# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         result = list(map(lambda x:0,range((10**4*2)+1)))

#         for n in nums:
#             result[n]+=1            
#         print(result)
#         cursor = (len(result)//2)
#         print(cursor)

#         """
#         음수 index 관련 내용이 혼란스러울 수 있는데, 다음 내용을 기억
#         1. result [-1]은 result[len(result)-1]을 가리킨다는 점
#         2. 실제로 해당 문제풀이를 할 때는 직관적으로 index가 적용된다는 점
#         """

#         while k>0:
#             if result[cursor] >0:
#                 k-=1
#                 result[cursor]-=1
#             else :
#                 cursor-=1

#         return cursor                    
            
            
# result = Solution().findKthLargest(nums=[-1,5,3,2,5,2,-2], k = 1)        
# print(result)
# Solution().findKthLargest(nums=[3,2], k = 2)        
# Solution().findKthLargest(nums=[3,2,1,5,6,4], k = 2)        
# Solution().findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k = 4)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        cursor = len(nums)-1
        current_max = nums[cursor]
                
        for i in range(len(nums)-2,-1,-1):
            if k == 1:
                return current_max
            else:
                current_max=nums[i]
                k-=1                
        
        return current_max


print(Solution().findKthLargest(nums=[-1], k = 1)) 
print(Solution().findKthLargest(nums=[-1,5,3,2,5,2,-2], k = 2)) 
print(Solution().findKthLargest(nums=[3,2], k = 2))
print(Solution().findKthLargest(nums=[3,2,1,5,6,4], k = 2))        
print(Solution().findKthLargest(nums=[3,2,3,1,2,4,5,5,6], k = 4))