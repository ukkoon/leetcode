from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length

        self.reverse_sublist(nums,0,length)
        self.reverse_sublist(nums,0,k)
        self.reverse_sublist(nums,k,length)                
        
    def reverse_sublist(self,lst,start,end):
        lst[start:end] = lst[start:end][::-1]
        return lst