'''
Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

https://youtu.be/WQMURqqQxk8?feature=shared&t=418
'''

class Solution:
    #from typing import List
    #def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits: int) -> int:
        
        #Method 1
        # number = int(''.join(map(str, digits)))
        # number = number + 1
        # arr = []
        # for num in str(number):
        #     arr.append(int(num))
        # return arr

        #Method 2
        # return [int(x) for x in str(int("".join([str(i) for i in digits])) + 1)]

        # Method 3 - reverse list addition
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


x = Solution()
print(x.plusOne([9,9,9]))