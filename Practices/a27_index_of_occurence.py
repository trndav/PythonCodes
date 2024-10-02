# Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)        

        # if not needle:
        #     return 0
        
        # # Get lengths of both strings
        # h_len = len(haystack)
        # n_len = len(needle)
        
        # # Slide the window over the haystack
        # for i in range(h_len - n_len + 1):
        #     # Check if the substring matches the needle
        #     if haystack[i:i + n_len] == needle:
        #         return i
        
        # # If no match found, return -1
        # return -1       

x = Solution()
print(x.strStr("sadbutsad", "sad"))