class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(":")","{":"}","[":"]"}        
        lefts = ['(','{','[']

        rights = []

        for i in range(len(s)):
            if s[i] in lefts:
                rights.append(brackets[s[i]])
            else:
                if not rights or s[i] != rights.pop():
                    return False

        return not rights

print(Solution().isValid("["))            
print(Solution().isValid("]"))
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("{([()]}}"))