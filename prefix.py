class Solution(object):
    def longestCommonPrefix(self, strs):
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""

        # Initialize the result as an empty string
        res = ""

        # Loop through the characters of the first string
        for i in range(len(strs[0])):
            # Check the current character in the first string against all strings
            for j in strs:
                # If we reach the end of any string or the characters do not match
                if i >= len(j) or j[i] != strs[0][i]:
                    return res  # Return the result so far
            # If the character matched for all strings, add it to the result
            res += strs[0][i]

        return res  # Return the final result

# Example usage:
strs = ["keko", "keow", "keght"]
solution = Solution()
print(solution.longestCommonPrefix(strs))  # Output: "ke"
