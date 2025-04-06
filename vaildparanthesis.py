def isValid(s):
    if '(' in s:
        if ')' not in s:
            return bool(0)
        return bool(1)
        

    if '{' in s:
        if '}' not in s:
            return bool(0)
        return bool(1)
    
        
    if '[' in s:
        if ']' not in s:
            return bool(0)
        return bool(1)
    
    #testing for vaild parenthesis

s= "{}"
result = isValid(s)
print(result)
    
            
    
        
       