from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums:List[int])->int:
        l = list(0 for n in range(60001))
        for i in nums:
            l[i]+=1     

        index = l.index(1)
        return index if index<=30000 else index-60001



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x ^ y, nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        
        return res