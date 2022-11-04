# set을 이용한 방법 (n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
        longestLen = 0
        for i in range(len(s)):
            substr = set(s[i])
            for j in range(i+1, len(s)):
                if s[j] in substr:
                    break
                substr.add(s[j])
            if len(substr)>longestLen:
                longestLen=len(substr)

        return longestLen

# Sliding Window technic