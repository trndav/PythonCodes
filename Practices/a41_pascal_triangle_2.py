
# Pascal's Triangle II

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]

class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        
        def generate(numRows: int) -> [[int]]:
        
            triangle = []
            for i in range(numRows):
                row = [1] * (i + 1)

                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                
                triangle.append(row)

            return triangle 

        y = generate(rowIndex+1)
        a = y[rowIndex]
        return a

x = Solution()
print(x.getRow(3))