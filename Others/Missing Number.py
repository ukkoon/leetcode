from typing import List


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         result = list(None for _ in range(len(nums)+1))        
#         for i in nums:
#             result[i]=i
        
#         return result.index(None)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        result = list(n for n in range(len(nums)+1))                
        return sum(result)-sum(nums)
            

print(Solution().missingNumber(nums=[9,6,4,2,3,5,7,0,1]))