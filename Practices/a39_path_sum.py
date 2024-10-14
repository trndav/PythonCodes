# Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:

        if not root:
            return False
            
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        
        # Check if we've reached a leaf node and the remaining targetSum is 0
        if not root.left and not root.right:  # It's a leaf
            return targetSum == 0
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    


def buildTreeFromList(values: [int]) -> [TreeNode]:
    if not values:
        return None
    
    # Create the root of the tree
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    # Build the tree using a queue (Breadth-first approach)
    while queue and i < len(values):
        current = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

root_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = buildTreeFromList(root_list)

# Create a Solution object and test the `hasPathSum` method
sol = Solution()
targetSum = 22
result = sol.hasPathSum(root, targetSum)
print(result)  # This should print True for this example
