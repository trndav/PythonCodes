# Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge cases where any number is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result as an array of zeros to store intermediate results
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        print("result:", result, m, n)
        
        # Reverse both numbers for easier multiplication from right to left
        num1, num2 = num1[::-1], num2[::-1]
        print(num1, num2)
        
        # Perform multiplication digit by digit
        for i in range(m):
            print("i in range m", i, m)
            for j in range(n):
                print(j, n)
                # Multiply digits and add to the result array at the correct position
                product = int(num1[i]) * int(num2[j])
                print(num1[i], num2[j])
                print(product)
                result[i + j] += product
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Convert result array back to string and remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))
    
x = Solution()
print(x.multiply("2", "3"))