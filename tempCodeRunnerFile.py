def isValid(s):
    if '(' in s:
        if ')' not in s:
            return print("not valid")
        return print("valid")
        

    if '{' in s:
        if '}' not in s:
            return print("not valid")
        return print("valid")
    
        
    if '[' in s:
        if ']' not in s:
            return print("not valid")
        return print("valid")
    
    #testing for vaild parenthesis

s= "("
result = isValid(s)
print(result)
    
            
    
        
       