
# Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously 
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer 
# is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
    

# Helper function to create a linked list from a list and an optional cycle
def createLinkedList(values, pos):
    if not values:
        return None
    
    # Create the head node
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    # Create the linked list
    for i in range(1, len(values)):
        new_node = ListNode(values[i])
        current.next = new_node
        current = new_node
        if i == pos:  # Keep track of the node where cycle should connect
            cycle_node = new_node
    
    # Create a cycle if pos is valid
    if pos != -1:
        current.next = cycle_node  # Point the last node to the cycle_node
    
    return head

# Example 1: [3,2,0,-4], pos = 1
values = [3, 2, 0, -4]
pos = 1
head = createLinkedList(values, pos)

# Check if there's a cycle
solution = Solution()
print("Has cycle:", solution.hasCycle(head))  # Expected: True