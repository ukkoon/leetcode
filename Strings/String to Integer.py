class Solution:
    def myAtoi(self, s: str) -> int:        
        ops = ['+','-']
        min = -2**31
        max = (2**31) -1
        ss = list(filter(lambda s:s, s.split(' ')))
        for s in ss:
            buffer = []
            for c in s:
                if c.isalpha() or c=='.':
                    break
                elif c in ops and buffer:
                    break
                else:
                    buffer.append(c)                    
            
            try:
                result = int(''.join(buffer))
                if min<result<max:
                    return result
                elif min>=result:
                    return min
                else:
                    return max
            
            except:
                break

        return 0
                


print(Solution().myAtoi("123-"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi(""))
print(Solution().myAtoi("words with +1321"))
print(Solution().myAtoi("   +0 123"))
print(Solution().myAtoi("21474836460"))
print(Solution().myAtoi("+-21"))
print(Solution().myAtoi("+21-43"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("-91283472332"))
print(Solution().myAtoi("3.14159"))
#-2147483648
# print(Solution().myAtoi('words and 987'))
# print(Solution().myAtoi('0032'))
# print(Solution().myAtoi("   -42"))
# print(Solution().myAtoi("asdf -dsaf21 21d9932 ds42"))        