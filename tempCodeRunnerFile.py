def two_sum(nums, target):
    num_map = {}  # Dictionary to store (value, index)

    for i, num in enumerate(nums):
        complement = target - num  # Find the required pair
        
        if complement in num_map:  # Check if complement exists
            return [num_map[complement], i]  # Return indices
        
        num_map[num] = i  # Store the current number in the dictionary
    
    return []  # Return empty if no solution found

# Example usage:
nums = [10, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)  # Output: Indices: [0, 1]
