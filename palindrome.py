def isPalindrome(x):
     
        # Step 1: Convert the number to a string
        num_str = str(x)
        
        # Step 2: Initialize pointers for the first and last digits
        left = 0
        right = len(num_str) - 1
        
        # Step 3: Compare the first and last digits
        while left < right: #0 < 2 
            if num_str[left] != num_str[right]: #if num_str[0] != num_str[2]., num_str[0] = 1, num_str[2] = 2
                return False  # If digits don't match, it's not a palindrome
            left += 1  # Move the left pointer inward
            right -= 1  # Move the right pointer inward
        
        return True  # If all pairs matched, it's a palindrome
result = isPalindrome(121) # Example usage
print(result)  # Output: True