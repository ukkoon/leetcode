from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                for j in range (i+1,n):
                    if nums[j] != 0:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] =tmp
                        break
        
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         for j in range(nums.count(0)):
#             nums.remove(0)
#             nums.append(0)