# Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: [TreeNode]) -> [int]:
        result = []
        
        def traverse(node):
            if node:
                # First, recur on the left child
                traverse(node.left)
                # Then, recur on the right child
                traverse(node.right)
                # Finally, process the root (current node)
                result.append(node.val)
        
        traverse(root)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
x = Solution()

print(x.postorderTraversal(root))  # Output: [3, 2, 1]