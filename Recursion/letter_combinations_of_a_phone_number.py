from typing import List


mappings = {
    "2":["a","b",'C'],
    "3":["d","e",'f'],
    "4":["g","i","h"]
}

result = []

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.comb(mappings)
    
    def comb(self, digits: str, cur:str)->List[str]:
        if len(digits) is 1:
            return cur+self.comb()
        else 
            return
        # if len(digits) is 1:
            