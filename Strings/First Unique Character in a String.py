# First Trying. ugly and not good at performance #

# class Solution:
#     def firstUniqChar(self, s: str) -> int:                    
#         one_times = []
#         losers = []
        
#         for c in range(len(s)):  
#             if s[c] in losers:
#                 continue            
#             elif s[c] not in one_times:
#                 one_times.extend(s[c])
#             else:
#                 one_times.remove(s[c])
#                 losers.extend(s[c])
        
#         try:
#             return s.index(one_times[0])
#         except:
#             return -1

# High performance pretty code #

class Solution:
    def firstUniqChar(self, s: str) -> int:            
        for char in s:    
            if s.index(char) == s.rindex(char):
                return s.index(char)                
        return -1

# more High performance ugly code #

# class Solution:
#     def firstUniqChar(self, s: str) -> int:        
#         losers = [ ]    
#         for char in s:    
#             if char in losers:
#                 continue

#             first_index = s.index(char)
#             if first_index == s.rindex(char):
#                 return first_index
#             else:
#                 losers.extend(char)
                
#         return -1