class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        
        keys = list(roman.keys())[::-1]      
        result = 0
        
        while s:
            for key in keys:
                if s.startswith(key):
                    s = s.replace(key,"",1)
                    result+=roman[key]
                    break
        return result

Solution().romanToInt("MCMXCIV")

