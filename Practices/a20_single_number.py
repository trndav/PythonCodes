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
        
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                del counts[n]
        return list(counts.keys())[0]

x = Solution()
print(x.singleNumber([2,2,3]))  # Should output 5 not 4