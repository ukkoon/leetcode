from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = nums.copy()

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums