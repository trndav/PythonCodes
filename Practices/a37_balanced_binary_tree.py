# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return 0  # Base case: height of an empty subtree is 0
            
            # Recursively get the heights of the left and right subtrees
            left_height = check_balance_and_height(node.left)
            right_height = check_balance_and_height(node.right)
            
            # If either subtree is unbalanced, propagate the failure by returning -1
            if left_height == -1 or right_height == -1:
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree (1 + max of left and right heights)
            return max(left_height, right_height) + 1
        
        # Use the helper function to determine if the tree is balanced
        return check_balance_and_height(root) != -1

root = TreeNode(3)                  # root node
root.left = TreeNode(9)             # left child of root
root.right = TreeNode(20)           # right child of root
root.right.left = TreeNode(15)      # left child of node 20
root.right.right = TreeNode(7)      # right child of node 20

# Now test the tree with your isBalanced function
solution = Solution()
print(solution.isBalanced(root))  # Output should be True
