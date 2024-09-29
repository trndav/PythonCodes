'''
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # Create a dummy node to start the new merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            # Compare the values of the current nodes
            if list1.val < list2.val:
                current.next = list1  # Attach list1's node to the merged list
                list1 = list1.next  # Move list1 to the next node
            else:
                current.next = list2  # Attach list2's node to the merged list
                list2 = list2.next  # Move list2 to the next node
            current = current.next  # Move the current pointer forward
        
        # Attach the remaining nodes from either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, skipping the dummy node
        return dummy.next
    
# Manually creating list1: [1,2,4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Manually creating list2: [1,3,4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
x = Solution()
merged_list = x.mergeTwoLists(list1, list2)

# Function to print the merged linked list
def print_linkedlist(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_linkedlist(merged_list)
