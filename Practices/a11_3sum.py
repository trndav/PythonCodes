'''
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: int): # -> List[List[int]]:
        
        #Brute force
        # if len(nums) < 3:
        #     return([])        
        # triplets = []
        # for i in range(0, len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if (nums[i] + nums[j] + nums[k]) == 0:
        #                 triplets.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        # return(list(set(triplets)))


        # n^2 solution with sorting
        # if len(nums) < 3:
        #     return([])        
        # triplets = []

        # nums = sorted(nums)
        # for i in range(0, len(nums)-2):
        #     lower = i + 1
        #     upper = len(nums) - 1

        #     while lower < upper:
        #         s = nums[i] + nums[lower] + nums[upper]
        #         if s == 0:
        #             triplets.append((nums[i], nums[lower], nums[upper]))
        #             lower += 1
        #         elif s < 0:
        #             lower += 1
        #         else:
        #             upper -= 1
        # return (list(set(triplets)))


        # n^2 solution with sorting - faster version
        if len(nums) < 3:
            return([])        
        triplets = []
        nums = sorted(nums)

        for i in range(0, len(nums)-2):            
            if nums[i] > 0:
                break 
            if nums[i] == nums[i-1] and i > 0:
                continue 

            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                if s == 0:
                    triplets.append((nums[i], nums[lower], nums[upper]))                    
                    
                if s <= 0:
                    lower += 1
                    while (nums[lower] == nums[lower - 1] and lower < upper):
                        lower += 1
                else:
                    upper -= 1

        return (triplets)


x = Solution()
print(x.threeSum([-1,0,1,2,-1,-4]))