# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev_node = None
        current_node = head
        
        while current_node:
            temp_head = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_head
            
        return prev_node
      
