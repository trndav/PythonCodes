# Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well. 

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        current = head 
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def list_to_linkedlist(lst):
    head = ListNode(lst[0])
    current = head 
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next 
    return head

# Helper function to convert a linked list back to a list
def linkedlist_to_list(node):
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result

x = Solution()
head1 = list_to_linkedlist([1,1,2])
result1 = x.deleteDuplicates(head1)
print(linkedlist_to_list(result1))

