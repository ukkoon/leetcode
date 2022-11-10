from typing import List

# Dutch national flag problem
# first try
class Solution:    
    def sortColors(self, nums: List[int]) -> None:
        lowest_index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i,lowest_index+1,-1):
                    nums[j]=nums[j-1]
                nums[lowest_index+1]=0
                lowest_index+=1

        for i in range(lowest_index+1,len(nums)):
            if nums[i] == 1:
                for j in range(i,lowest_index+1,-1):
                    nums[j]=nums[j-1]
                nums[lowest_index+1]=1
                lowest_index+=1


nums=[2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)

nums=[2,0,1]
Solution().sortColors(nums)
print(nums)

nums=[2,2,2,1,1,0,2,2,2,1,1,1,1,1,1,0,1,0,2,1,1]
Solution().sortColors(nums)
print(nums)     
        