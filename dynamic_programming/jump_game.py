from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        지금 점프대에서 가능한 멀리 뛰는 것이 아니라,
        가장 멀리 뛸 수 있는 점프대까지 뛰며 이동하는 모습을 연상해보자.
        """
        max_jump_pad = 0

        # 가장 멀리 뛸 수 있는 점프대가 0칸짜리 점프대라면 탐색 끝
        while nums[max_jump_pad]!=0:
            # 한 점프대에서 도달할 수 있는 마지막 인덱스까지 체크를 해야한다.
            for i in range(max_jump_pad, max_jump_pad+nums[max_jump_pad]+1):
                candidate = i + nums[i]                

                if candidate>=len(nums)-1:
                    return True
                    
                elif candidate>=max_jump_pad+nums[max_jump_pad]:
                    max_jump_pad=i
                
        # return False except only len(nums) is 1
        return len(nums) == 1

# Reference
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            
            if i + nums[i] >= goal:
                
                goal = i
                
        return goal == 0 # True if goal == 0 else False

result = Solution().canJump(nums=[5,9,3,2,1,0,2,3,3,1,0,0])
print(result)

result = Solution().canJump(nums=[0])
print(result)

result = Solution().canJump(nums=[2,0,0])
print(result)

result = Solution().canJump(nums=[1,2,3])
print(result)

result = Solution().canJump(nums=[1,2,3,100,0,2,1])
print(result)

result = Solution().canJump(nums=[1,1,1,1,1,1,1,1,1,2,3,0,0,2,1])
print(result)

result = Solution().canJump(nums=[2,3,1,1,4])
print(result)

result = Solution().canJump(nums=[3,2,1,0,4])
print(result)
