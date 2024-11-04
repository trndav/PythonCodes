# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_pos = mid  # potential first position
                    right = mid - 1  # look for earlier instances
            return first_pos

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last_pos = mid  # potential last position
                    left = mid + 1  # look for later instances
            return last_pos

        # Find the first and last position
        first_pos = find_first(nums, target)
        last_pos = find_last(nums, target)

        return [first_pos, last_pos] if first_pos != -1 else [-1, -1]

x = Solution()
print(x.searchRange([5,7,7,8,8,10], target = 8))