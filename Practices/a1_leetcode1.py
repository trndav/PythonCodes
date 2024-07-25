class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # First solution (slow)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if num[i] + nums[j] == target:
        #             return([i, j])
                
        # Second solution
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num] = i 
                
