'''
Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        path = {1:1, 2:2, 3:3, 4:5}
        for x in range(5, n+1):
            path[x] = path[x-1] + path[x-2]
        print(path)
        return path[n]


x = Solution()
print(x.climbStairs(6))