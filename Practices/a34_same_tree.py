
# Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:

        if not p and not q:
            return True

        # If one of the nodes is None or values do not match, trees are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#         if p == q:
#             return True

# from collections import deque

# def build_tree_from_list(values):
#     if not values:
#         return None
#     root = TreeNode(values[0])
#     queue = deque([root])
#     i = 1
#     while i < len(values):
#         current = queue.popleft()
        
#         if values[i] is not None:
#             current.left = TreeNode(values[i])
#             queue.append(current.left)
#         i += 1
        
#         if i < len(values) and values[i] is not None:
#             current.right = TreeNode(values[i])
#             queue.append(current.right)
#         i += 1
    
#     return root

# p = [1,2]
# q = [1,None,2]
# p1 = build_tree_from_list(p)
# q1 = build_tree_from_list(q)

# x = Solution()
# result = x.isSameTree(p, q)
# print(result)