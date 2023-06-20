from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = list(strs)
        result = []    

        for i in range(len(strs)):
            characters = list(strs[i])
            characters.sort()
            strs[i] = "".join(characters)
        
        checked = []

        for i in range(len(strs)):
            target = strs[i]
            if target in checked:
                continue
            else:
                checked.append(target)
                indices = [i]
                for j in range(i+1,len(strs)):
                    if target == strs[j]:
                        indices.append(j)

                anagram = []
                for result_index in indices:
                    # print(copy[result_index])
                    anagram.append(copy[result_index])
                result.append(anagram)
                

        return result
    

result = Solution().groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"])
print(result)