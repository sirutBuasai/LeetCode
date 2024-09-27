# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev_node = None

        while head:
            temp_head = head.next
            head.next = prev_node
            prev_node = head
            head = temp_head

        return prev_node


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev_node = None

        while head.next:
            temp_head = head.next
            head.next = prev_node
            prev_node = head
            head = temp_head

        head.next = prev_node

        return prev_node
