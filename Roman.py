def romanToInt(s):
       
        # Step 1: Map of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # This will store the final result

        # Step 2: Loop through the string
        for i in range(len(s)):
            current_value = roman_map[s[i]] # we put s[i] in the roman_map to get the value of the current roman number in the dictionary.

            # Step 3: Check if this is a subtractive case
            if i < len(s) - 1 and current_value < roman_map[s[i + 1]]:
                total -= current_value
            else:
                total += current_value

        return total
# Example usage:
result = romanToInt("IV")  # Example usage
print(result)  # Output: 3