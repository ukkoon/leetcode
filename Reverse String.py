from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        right=len(s)-1
        for i in range(0, (right//2)+1, 1):
            temp=s[i]
            s[i]=s[right]
            s[right]=temp
            right-=1


s = ["h","e","l","o","w"]

Solution().reverseString(s=s)
print(s)

        