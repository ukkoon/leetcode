from typing import List

mappings = {
    "2":["a","b",'c'],
    "3":["d","e",'f'],
    "4":["g","i","h"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["q","p","r","s"],
    "8":["t","u","v"],
    "9":["w","y","x","z"]
}

class Solution:
    result = []
    def letterCombinations(self, digits: str) -> List[str]:
        """
        iterative strategy 더욱 효과적일 것 같지만 문제의 요구사항대로 recursive strategy를 적용
        """
        self.result=[]        
        if digits:
            self.comb(digits,"")        
        return self.result
    
    def comb(self, digits:str, cur:str)->List[str]:        
        if len(cur) == len(digits):
            self.result.append(cur)
            return
        else:
            for d in mappings[digits[len(cur)]]:                
                self.comb(digits,cur+d)

print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("45"))