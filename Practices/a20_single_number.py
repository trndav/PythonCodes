'''
Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
'''

class Solution:
    #def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums) -> int:
        
        # Method 1
        # counts = {}
        # for n in nums:
        #     if n not in counts:
        #         counts[n] = 1
        #     else:
        #         del counts[n]
        # return list(counts.keys())[0]

        # Method 2
        # x = 0
        # for i in range(len(nums)):
        #     x = x^nums[i]
        #     print("i", i)
        #     print("nums[i]", nums[i])
        #     print("x^nums[i]", x^nums[i])
        #     print(x)
        # return x

        # Method 3 XOR
        
        a = 0
        for i in nums:
            a ^= i # ^bitwise XOR operator, cancel each bit, so for 2 and 2 = 0
            print("a is:", a)
        return a

x = Solution()
print(x.singleNumber([2,2,3,3,4]))  # Should output 5 not 4