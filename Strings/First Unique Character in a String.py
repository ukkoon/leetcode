class Solution:
    def firstUniqChar(self, s: str) -> int:                    
        one_times = []
        losers = []
        
        for c in range(len(s)):  
            if s[c] in losers:
                continue            
            elif s[c] not in one_times:
                one_times.extend(s[c])
            else:
                one_times.remove(s[c])
                losers.extend(s[c])
        
        try:
            return s.index(one_times[0])
        except:
            return -1