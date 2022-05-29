from functools import reduce
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strN = reduce(lambda x,y: f"{x}"+f"{y}", digits)
        intN = int(strN)
        intN += 1
        strN = str(intN)
        return list(map(lambda x:int(x) , strN))
        
print(Solution().plusOne(digits=[9]))
print(Solution().plusOne(digits=[1,2,3,4,5]))