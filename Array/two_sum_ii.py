from typing import List

#solve o(1) space complexity
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        numbers.sort()
        left = 0
        right = len(numbers)-1
        
        while right>left:
            candidate = numbers[left]+numbers[right]

            if candidate == target:
                return [left,right]
            elif candidate<target:
                left+=1
            else:
                right-=1
            # j = numbers[i+1:].index(subtarget)
            # print(j)
            # if j:
            #     return [i+1,j+1]
            
            

            

# print(Solution().twoSum(list(map(lambda x:-1,range(0,3*10**4))),target=2))              
print(Solution().twoSum([-1,-2,-3,-4,-5],target=-8))                
print(Solution().twoSum([0,4,3,0],target=0))
print(Solution().twoSum([2,7,11,15],target=9))
print(Solution().twoSum([3,2,4],target=6))
print(Solution().twoSum([5,25,75],target=100))