# Excel Sheet Column Title
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:
# A -> 1
# B -> 2
# C -> 3

# Z -> 26
# AA -> 27
# AB -> 28 

# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        result = []
        
        while columnNumber > 0:
            # Find remainder and adjust for zero-indexed calculation
            columnNumber -= 1
            remainder = columnNumber % 26
            print(remainder)
            # Convert to corresponding letter
            result.append(chr(remainder + ord('A')))
            # Update columnNumber
            columnNumber //= 26
        
        # Reverse the result as we build it backwards
        return ''.join(result[::-1])

x = Solution()
print(x.convertToTitle(701))

# print(ord('A'))
# columnNumber = 18
# columnNumber -= 1
# print(columnNumber)
# print(chr(70))
# columnNumber //= 2
# print(columnNumber)
# result = [1,2,3]
# print(result[::-1])