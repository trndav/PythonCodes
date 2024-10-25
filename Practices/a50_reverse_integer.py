# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine if the number is negative
        sign = -1 if x < 0 else 1
        # Remove the sign for the reversing process
        x = abs(x)
        
        # Reverse the digits by converting to string, reversing, and converting back
        reversed_num = int(str(x)[::-1])
        
        # Restore the sign
        reversed_num *= sign
        
        # Check if the reversed number is within the 32-bit integer range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        
        return reversed_num

x = Solution()
print(x.reverse(120))