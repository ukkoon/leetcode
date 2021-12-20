from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastCursor = 0

        for i in range(0,len(nums)):
            if nums[i]>nums[lastCursor]:
                lastCursor+=1
                nums[lastCursor]=nums[i]

        return lastCursor+1
