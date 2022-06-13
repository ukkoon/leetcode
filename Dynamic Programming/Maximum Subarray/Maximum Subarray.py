import math
from threading import local
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_maximum = -float('inf')
        global_maximum = -float('inf')

        for i in range(len(nums)):             
            local_maximum = max(nums[i], nums[i]+local_maximum)            
            global_maximum = max(local_maximum,global_maximum)
            

        return global_maximum

# 헷갈림 방지 주석
# global_maximum = 60인 상황에서
# [10 ,20 ,30 ,-60, 80], i = 3인 경우 
# local_maxiumu이 max(-60, 10+20+30-60)을 통해 0에 머문다.
# global_maximum은 60이 유지된다.

# [10 ,20 ,30 ,-60, 80], i = 4인 경우 
# local_maxiumu이 max(0, 0+80)을 통해 80에 머문다.
# global_maximum이 80으로 경신된다.



# global_maximum = 60인 상황에서
# [10 ,20 ,30 ,-10, 80], i = 3인 경우 
# local_maxiumu이 max(-10, 10+20+30-10)을 통해 50에 머문다.
# global_maximum은 60이 유지된다.

# [10 ,20 ,30 ,-10, 80], i = 4인 경우 
# local_maxiumu이 max(80, 50+80)을 통해 130에 머문다.
# global_maximum이 130으로 경신된다.