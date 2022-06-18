from re import sub
from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:        
#         n = len(nums)
#         for i in range(n):            
#             if nums[i]!=target or nums[i] <= target:
#                 subtarget = target - nums[i]
#                 for j in range(i+1,n):      
#                     if nums[j] == subtarget:
#                         return [i,j]

class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        indicies = {}
        for i in range(len(nums)):            
            subtarget = target - nums[i]
            if subtarget in indicies:
                return [i,indicies[subtarget]]            
            indicies[nums[i]]=i
            

            

   


print(Solution().twoSum([-1,-2,-3,-4,-5],target=-8))                
print(Solution().twoSum([0,4,3,0],target=0))
print(Solution().twoSum([2,7,11,15],target=9))
print(Solution().twoSum([3,2,4],target=6))

        