from typing import List

class Solution:
    def reverse(self, x: int) -> int:                
        isPos=1 if x>=0 else -1
        s = list(str(x).replace('-',''))
        cursor = len(s)-1
        
        for i in range(0,(cursor//2)+1):
             temp=s[i]
             s[i]=s[cursor]
             s[cursor]=temp
             cursor-=1        

        n = int(''.join(s))*isPos
       
        return n if abs(n) < 2**31 and n != 2**31 - 1 else 0