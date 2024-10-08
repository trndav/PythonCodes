# Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

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
    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        def inorder(node):
            if not node:
                return []
            # Traverse left subtree, then root, then right subtree
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        return inorder(root)

# Helper function to build a binary tree from a list using level order
from collections import deque

def build_tree_from_list(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        current = queue.popleft()
        
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    
    return root

# Example usage:
values = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
root = build_tree_from_list(values)

x = Solution()
result = x.inorderTraversal(root)
print(result)