# 26. Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:

        if not nums:
            print("The list is empty.")

        # Two pointers: 'i' is the slow-runner, 'j' is the fast-runner
        i = 0  # slow pointer (marks the position for unique elements)

        # Iterate through the array 
        for j in range(1, len(nums)):
            # If the current number is different from the last unique one
            if nums[j] != nums[i]:
                i += 1  # Move the slow pointer forward
                nums[i] = nums[j]  # Update the position with the new unique value

        # 'i + 1' is the number of unique elements
        return i + 1

x = Solution()
print(x.removeDuplicates([1,1,2,2,3]))
print(x.removeDuplicates([]))