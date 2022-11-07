from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        left = 0
        right = len(nums)-1
        
        for i in range(len(nums)):
            target = nums[left] + nums[right]
            result = self.twoSum(nums[i+1:], target)
            print(result)
                        
        

    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        numbers.sort()
        left = 0
        right = len(numbers)-1
        result = []
        while right>left:
            candidate = numbers[left]+numbers[right]
            if candidate == target:
                result.append ([left,right])
            elif candidate<target:
                left+=1
            else:
                right-=1

        return result
            
        

print(Solution().threeSum([1,2,-2,-1]))
print(Solution().threeSum([0,0,0]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,1,2]))
# print(Solution().threeSum([-1,0,1,2,-1,-4,3,4,7,3,1,4,7,3,2,2,2,2,1,5,2,3,5,7,-4,-2,-7,-5,-2]))
#[[-7,0,7],[-7,2,5],[-7,3,4],[-5,-2,7],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-1,5],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,-1,2],[-1,0,1]]
# [[-1, 0, 1], [-1, -1, 2], [-2, 1, 1], [-4, 2, 2], [-5, -2, 7], [-5, 2, 3], [-2, -1, 3], [-7, 3, 4], [-5, 1, 4], [-2, 0, 2], [-4, 1, 3], [-7, 2, 5], [-2, -2, 4], [-4, 0, 4], [-4, -1, 5], [-5, 0, 5], [-7, 0, 7]]
# [[1, 0, -1], [-2, 1, 1], [-5, 3, 2], [5, -1, -4], [7, -2, -5], [4, -2, -2], [-4, 2, 2], [-1, 1, 0], [-7, 4, 3], [2, -1, -1], [3, -1, -2], [0, 1, -1]]