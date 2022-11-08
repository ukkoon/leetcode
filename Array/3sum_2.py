from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        cursor = 0        

        while cursor < len(nums)-1:           
            if nums[cursor]>0:
                break            
            elif cursor==0 or nums[cursor] != nums[cursor-1]:
                result.extend(self.twoSum(nums[cursor+1:], -nums[cursor]))                       
            cursor+=1               
        
        return result                            

    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        left = 0
        right = len(nums)-1
        result = []
        # nums[left] is always unique.
        while right>left:
            candidate = nums[left]+nums[right]
            if candidate<target:
                left+=1
            elif candidate>target:
                right-=1
            else:      
                #해당 left, right쌍은 고유하므로...
                result.append([-target,nums[left],nums[right]])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
        return result        
        

# print(Solution().threeSum(list(map(lambda x:-1,range(3000)))))
# print(Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
# print(Solution().threeSum([1,2,-2,-1]))
# print(Solution().threeSum([0,0,0]))
# print(Solution().threeSum([-1,0,1,2,-1,-4,-1]))
# print(Solution().threeSum([-1,0,1,2,-1,-9,-1,-1,-1,-1,-1]))
# print(Solution().threeSum([0,1,2]))
# print(Solution().threeSum([-1,0,1,2,-1,-4,3,4,7,3,1,4,7,3,2,2,2,2,1,5,2,3,5,7,-4,-2,-7,-5,-2]))