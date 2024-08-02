'''
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

class Solution:
    def maxArea(self, height: [int]) -> int:

        start = 0
        end = len(height) -1
        largest = 0

        while start < end:
            next_area = min(height[start], height[end]) * (end - start)

            if next_area > largest:
                largest = next_area

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return largest
    
x = Solution()
print(x.maxArea([1,8,6,2,5,4,8,3,7]))
