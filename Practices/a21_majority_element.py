'''
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    #def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums) -> int:

        # Method 1
        # sums = {}
        # for n in nums:
        #     if n not in sums:
        #         sums[n] = 1
        #     else:
        #         sums[n] += 1
            
        #     if sums[n] > len(nums)/2:
        #         return n

        #Method 2
        # x = sorted(nums)
        # return x[len(x)//2]

        # Shorter
        return sorted(nums)[len(nums)//2]

x = Solution()
print(x.majorityElement([3,2,3])) 
print(x.majorityElement([2,2,1,1,1,2,2])) 
print(x.majorityElement([1,2,2,3,4]))