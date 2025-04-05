def longestCommonPrefix(strs):
   res = ""

   for i in range(len(strs[0])):
        for j in strs:
            if i == len(j) and j[i] != strs[0][i]:
                return res
            res += strs[0][i]

            return res

            
# Example usage:
strs = ["keko", "keow", "keght"]
print(longestCommonPrefix(strs))  # Output: "fl"