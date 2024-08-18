'''
Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
'''

class Solution:
    def mySqrt(self, x: int) -> int:

        # Method 1
        # import math
        # return int(math.sqrt(x))
        
        # Method 2 - not good for numbers like 8
        # counter = 0
        # adder = 0
        # while x != 0:
        #     x = x - (adder + 1)
        #     counter += 1
        #     adder = adder + 2
        #     print(x)
        # return counter // 1

        # Method 3 exponent solution
        # return int(x**(1/2))

        # Some method
        i = 0
        while i*i < x:
            i+=1
        if i*i == x:
            return i
        elif i*i > x:
            return i - 1

x = Solution()
print(x.mySqrt(8))