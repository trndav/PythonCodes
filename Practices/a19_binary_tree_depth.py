'''
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def listToTree(self, lst, index=0):
        if index >= len(lst) or lst[index] is None:
            return None

        root = TreeNode(lst[index])
        root.left = self.listToTree(lst, 2 * index + 1)
        root.right = self.listToTree(lst, 2 * index + 2)

        return root

x = Solution()
root = x.listToTree([3,9,20,None,None,15,7,11,89,33,7,71])
print(x.maxDepth(root))  # Should output 5 not 4
