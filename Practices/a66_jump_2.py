# Jump Game II
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if 
# you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # No jumps needed if we're already at the last index

        jumps = 0  # Number of jumps made
        current_end = 0  # The farthest index we can reach with current number of jumps
        farthest = 0  # The farthest index we can reach overall during the current traversal

        for i in range(n - 1):  # Iterate through the array up to the second-to-last element
            farthest = max(farthest, i + nums[i])  # Update the farthest index we can reach
            if i == current_end:  # We've reached the end of our current jump range
                jumps += 1  # Increment the jump count
                current_end = farthest  # Update the end of our current jump range
                if current_end >= n - 1:  # If we can reach or pass the last index
                    break

        return jumps

x = Solution()
print(x.jump([2,3,1,1,4,7,9]))