# Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.

# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        if not headA or not headB:
            return None
        
        # Initialize two pointers for both lists
        pA, pB = headA, headB
        
        # Traverse both lists
        while pA != pB:
            # Move to the next node or to the head of the other list if end is reached
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        # Either they meet at the intersection node or they both end as None
        return pA
    

def create_linked_lists(intersectVal, listA_vals, listB_vals, skipA, skipB):
    # Create the intersecting node if there's a valid intersection value
    intersection_node = ListNode(intersectVal) if intersectVal else None
    
    # Create List A up to the intersection
    headA = ListNode(listA_vals[0])
    currentA = headA
    for i in range(1, skipA):
        currentA.next = ListNode(listA_vals[i])
        currentA = currentA.next
    
    # Attach the intersection node to List A
    if intersection_node:
        currentA.next = intersection_node
        currentA = intersection_node
    
    # Continue creating List A if there are more values after the intersection
    for i in range(skipA + 1, len(listA_vals)):
        currentA.next = ListNode(listA_vals[i])
        currentA = currentA.next
    
    # Create List B up to the intersection
    headB = ListNode(listB_vals[0])
    currentB = headB
    for i in range(1, skipB):
        currentB.next = ListNode(listB_vals[i])
        currentB = currentB.next
    
    # Attach the intersection node to List B
    if intersection_node:
        currentB.next = intersection_node
    
    # Continue creating List B if there are more values after the intersection
    for i in range(skipB + 1, len(listB_vals)):
        currentB.next = ListNode(listB_vals[i])
        currentB = currentB.next
    
    return headA, headB

# Example input
intersectVal = 8
listA_vals = [4, 1, 8, 4, 5]
listB_vals = [5, 6, 1, 8, 4, 5]
skipA = 2
skipB = 3

# Create the linked lists
headA, headB = create_linked_lists(intersectVal, listA_vals, listB_vals, skipA, skipB)

# Find the intersection
sol = Solution()
intersection_node = sol.getIntersectionNode(headA, headB)

# Print the result
if intersection_node:
    print(f"Intersected at '{intersection_node.val}'")  # Output: Intersected at '8'
else:
    print("No intersection.")