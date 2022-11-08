from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = set()
        for i in range(len(nums)-1):
            target = nums[i]
            res = set(map(lambda x:(tuple(sorted([target, *list(x)]))),self.twoSum(nums[i+1:],-target)))                  
            result = result.union(res)

        return list(map(lambda x:list(x),list(result)))

    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        indicies = {}
        result = set()
        for i in range(len(nums)):            
            subtarget = target - nums[i]
            if subtarget in indicies:
                result.add((nums[i],nums[indicies[subtarget]]))
            indicies[nums[i]]=i
        return result