# first solution but it use python list indexer gimmick? 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:   
                if haystack[i:i+len(needle)]==needle:
                    return i             

        return -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if not needle:
#             return 0

#         for i in range(len(haystack)):
#             if haystack[i] == needle[0] and i+len(needle)<=len(haystack):
#                 count = 0
#                 for j in range(len(needle)):
#                     if haystack[i+j]==needle[j]:
#                         count+=1
#                     else:
#                         break
#                 if count == len(needle):
#                     return i

#         return -1

print(Solution().strStr("aaa","aaa"))