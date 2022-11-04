class Solution:
    # set을 이용한 방법 (n^2)
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
    def lengthOfLongestSubstring2(self, s:str) -> int:
        
        longest = cur = s[0] if s else ""

        for i in range(len(s)-1):
            if s[i+1] not in cur:
                cur+=s[i+1]
            else:
                cur = cur[cur.index(s[i+1])+1:]+s[i+1]
            if len(cur)>len(longest):
                longest=cur

        return len(longest)

