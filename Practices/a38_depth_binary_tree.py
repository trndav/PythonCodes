# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: [TreeNode]) -> int:

        if not root:
            return 0
        
        # If it's a leaf node (no children)
        if not root.left and not root.right:
            return 1
        
        # If the left subtree is None, check only the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If the right subtree is None, check only the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both left and right subtrees exist, return the minimum depth of the two
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


root = TreeNode(3)                  # root node
root.left = TreeNode(9)             # left child of root
root.right = TreeNode(20)           # right child of root
root.left.right = TreeNode(null)      # left child of node 20
root.left.left = TreeNode(null)      # right child of node 20
root.right.left.right = TreeNode(15)      # right child of node 20
root.right.left.left = TreeNode(7)  

# Now test the tree with your isBalanced function
solution = Solution()
print(solution.minDepth(root))  # Output should be True