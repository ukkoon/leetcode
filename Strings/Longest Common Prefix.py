from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens =  list(map(lambda x:len(x), strs))
        n = min(lens)

        for i in range(n,-1,-1):
            count = 0
            target = strs[0][0:i]
            for j in range(len(strs)):
                if target==strs[j][0:i]:
                    count+=1

            if count == len(strs):
                return strs[j][0:i]
                                                                        
        return ""