'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        # Inner string replace method
        replace = True 
        while replace:
            start_length = len(s)
            print(len(s))
            for inner in ["{}", "()", "[]"]:
                s = s.replace(inner, "")
            
            if start_length == len(s):
                replace = False
        
        return s == ""
        
x = Solution()
print(x.isValid("([)"))