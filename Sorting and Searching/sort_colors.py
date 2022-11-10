from typing import List
import time

# Dutch national flag problem (in-place)
class Solution:    
    def sortColors(self, nums: List[int]) -> None:
        low_index = 0
        
        # [0,0,0..., others]
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i], nums[low_index] = nums[low_index], nums[i]
                low_index+=1
        
        # [0,0,0,1,1,1,... others]
        for i in range(low_index,len(nums)):
            if nums[i]==1:
                nums[i], nums[low_index] = nums[low_index], nums[i]
                low_index+=1

# Reference (One-Way Solution)
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        
# nums=[2,0,1,1,0,1,2,0]
# Solution().sortColors(nums)
# print(nums)

# nums=[2,0,2,1,1,0]
# Solution().sortColors(nums)
# print(nums)

# nums=[2,0,1]
# Solution().sortColors(nums)
# print(nums)

# nums=[2]
# Solution().sortColors(nums)
# print(nums)     

nums = list(map(lambda x:x,range(0,5000000)))
start = time.time()
Solution2().sortColors(nums)
end = time.time()
# print(nums)
print(end-start)


nums = list(map(lambda x:x,range(0,5000000)))
start = time.time()
Solution().sortColors(nums)
end = time.time()
# print(nums)
print(end-start)

