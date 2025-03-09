from typing import Optional


# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):  # Correct constructor
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()  # Dummy node
        cur = d  # Pointer to traverse

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # Append the remaining nodes
        cur.next = list1 if list1 else list2
        return d.next


# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Input lists
l1_values = [1, 3, 4, 5, 6]
l2_values = [2, 3, 3, 4]

# Create linked lists
l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(l1, l2)

# Print the merged linked list
print("Merged Linked List:")
print_linked_list(merged_list)
