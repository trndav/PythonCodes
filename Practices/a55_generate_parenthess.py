# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        def backtrack(s='', open_count=0, close_count=0):
            # If the current string reaches the maximum length, add it to the results
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # Add an open parenthesis if we can
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            # Add a close parenthesis if it won’t lead to an imbalance
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        result = []
        backtrack()
        return result

x = Solution()
print(x.generateParenthesis(8))