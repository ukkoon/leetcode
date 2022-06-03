import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "".join(re.findall("[a-zA-Z0-9]", s))
        n = len(letters)
        print(letters)
        for i in range(0,(n//2)):
            if letters[i].upper() != letters[n-i-1].upper():
                return False
        return True
            


print(Solution().isPalindrome(s="0P"))