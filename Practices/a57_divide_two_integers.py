# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer 
# range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, 
# and if the quotient is strictly less than -231, then return -231.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define constants for the 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Edge case: if the divisor is 0 (though not specified, it’s good to check)
        if divisor == 0:
            raise ValueError("Division by zero is undefined")
        
        # Edge case: if dividend is INT_MIN and divisor is -1, return INT_MAX to prevent overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values to simplify
        dividend, divisor = abs(dividend), abs(divisor)

        # Quotient initialization
        quotient = 0

        # Using bitwise left shift to optimize subtraction
        # The idea is to "multiply" divisor by powers of two until it reaches dividend
        while dividend >= divisor:
            # Initialize variables for the shifting process
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            # Subtract the largest shifted divisor from the dividend
            dividend -= temp_divisor
            # Add the corresponding multiple to the quotient
            quotient += multiple

        # Apply the sign
        quotient = -quotient if negative else quotient

        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
    
x = Solution()
print(x.divide(-10, 3))