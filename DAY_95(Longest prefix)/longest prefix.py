def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix=strs[0]
    
    for  string in strs[1:]:
        
        while not string.startswith(prefix):
            
            prefix=prefix[:-1]
            
            if not prefix:
                return ""
    
    return prefix
            
strings=["flower","flow","flight"]
result=longest_common_prefix(strings)
print(f"Longest Common Prefix:'{result}' ")