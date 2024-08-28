'''
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Follow up: Could you minimize the total number of operations done?
'''

class Solution:
    #def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Method 1
        # for num in nums:
        #     if num == 0:
        #         nums.remove(num)
        #         nums.append(num)
        # return nums

        # Method 2

        zero_count = nums.count(0)
        next_non_zero = 0
        for n in nums:
            if n != 0:
                nums[next_non_zero] = n 
                next_non_zero += 1
        for zero in range(1, zero_count + 1):
            nums[-zero] = 0
            


x = Solution()
print(x.moveZeroes([0,1,0,3,12])) 
print(x.moveZeroes([0,1,0,3,12,0,1,0,3,12])) 