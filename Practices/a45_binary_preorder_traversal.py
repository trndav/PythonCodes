# Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]

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
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        
        # Not good
        # result = []
        # def traverse(node):
        #     if node:
        #         result.append(node.val)
        #         traverse(node.left)
        #         traverse(node.right)
        #     traverse(root)
        #     return result

        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()  # Get the current node
            result.append(node.val)  # Visit the node
            
            # Push right child first so that left child is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result