def decompress_length(s:str):    
    stack = s.replace(')','').split('(')[::-1]    
    result = len(stack[0])
    
    for n in stack[1:]:
        result = len(n[0:-1])+ (result * int(n[-1]))

    return result


compressed_string = input().strip()
print(decompress_length(compressed_string))
