# Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in 
# candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        def backtrack(start, target, path):
            # Base case: if the target is met, add the current path to the results
            if target == 0:
                results.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current candidate exceeds the target, stop further exploration
                if candidates[i] > target:
                    break
                # Recur with reduced target and updated path
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  # Sort to simplify duplicate handling
        results = []
        backtrack(0, target, [])
        return results

# Example usage:
solution = Solution()

# Example 1
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

# Example 2
print(solution.combinationSum2([2, 5, 2, 1, 2], 5))
# Output: [[1, 2, 2], [5]]