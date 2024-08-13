'''
Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
https://youtu.be/_zXpdlYQ0QQ?si=UR21J7SvE8jnsSxD&t=320
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Method 1
        # s = s.split()        
        # return len(s[-1])
        
        # Method 2
        # if s.split():
        #     return len(s.split()[-1])
        # return 0
    
        # Method 3 without split
        count = 0
        for letter in s[::-1]: #[::-1] reversed order
            if letter == " ":
                if count >= 1:
                    return count
            else:
                count += 1
        return count  

x = Solution()
print(x.lengthOfLastWord("Hello World"))
print(x.lengthOfLastWord(" "))