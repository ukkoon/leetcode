class Solution:
    # Sliding Window Algorithm
    def lengthOfLongestSubstring(self, s:str) -> int:                
        longest = cur = s[0] if s else ""        

        for i in range(len(s)-1):
            if s[i+1] not in cur:
                cur+=s[i+1]
            else:
                # ex)
                # cur이 "abcdefgh"인 경우, s[i+1]이 a면
                # cur의 값은 "bcdefgha"로 갱신
                cur = cur[cur.index(s[i+1])+1:]+s[i+1]                
            if len(cur)>len(longest):
                longest=cur

        return len(longest)

s = "pwbbbbasdwasdfnjkdsafbui23njknwwwwkew"
result = Solution().lengthOfLongestSubstring(s)
print(result)