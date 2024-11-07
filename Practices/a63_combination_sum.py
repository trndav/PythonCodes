# Combination Sum

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations 
# of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        result = []
        
        def backtrack(remaining, combo, start):
            # Base case: If the remaining sum is 0, we've found a valid combination
            if remaining == 0:
                result.append(list(combo))
                return
            
            # Iterate over the candidates starting from 'start' index
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                
                # Skip if the candidate exceeds the remaining sum
                if candidate > remaining:
                    continue
                
                # Choose the current candidate
                combo.append(candidate)
                
                # Explore further with the updated remaining sum
                backtrack(remaining - candidate, combo, i)  # 'i' allows the same element to be reused
                
                # Backtrack (remove the last chosen candidate)
                combo.pop()
        
        backtrack(target, [], 0)
        return result