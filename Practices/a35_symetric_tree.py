# Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True 
        
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True  # Both nodes are null, so they are symmetric
            if not left or not right:
                return False  # Only one node is null, they are not symmetric
            if left.val != right.val:
                return False  # Values are different, not symmetric
            
            # Recursively compare the left subtree of the left node with the right subtree of the right node,
            # and the right subtree of the left node with the left subtree of the right node.
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left, root.right)

from collections import deque
def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

# Example usage
tree_list = [1, 2, 2, 3, 4, 4, 3]
root = list_to_tree(tree_list)
x = Solution()
print(x.isSymmetric(root))  # Output should be True