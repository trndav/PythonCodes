# Linked list example
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
linked_list = LinkedList()

# Append elements to the linked list
linked_list.append(1)
linked_list.append(21)
linked_list.append(3)

# Print the linked list
linked_list.print_list()

# End
# ************

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        added = ListNode(val = (l1.val + l2.val) %10)
        carry_over = (l1.val + l2.val) // 10
        current_node = added

        while (l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next 

        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode(val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            current_node = current_node.next 

        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            current_node = current_node.next 

        if (carry_over) > 0:
            current_node.next = ListNode(val = 1)

        return(added)
    


def create_linked_list_from_list(lst):
    head = ListNode(lst[0])
    current_node = head
    for val in lst[1:]:
        current_node.next = ListNode(val)
        current_node = current_node.next
    return head

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Create two linked lists
l1 = create_linked_list_from_list([2, 4, 3])  # represents the number 342
l2 = create_linked_list_from_list([5, 6, 4])  # represents the number 465

# Add the two numbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

print_linked_list(result)
