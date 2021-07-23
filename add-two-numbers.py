# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_over = (l1.val + l2.val) // 10
        value = (l1.val + l2.val) % 10
        ans_list = ListNode(value)
        current_node = ans_list
        
        while(l1.next is not None or l2.next is not None or carry_over > 0):
            
            if l1.next is not None:
                l1 = l1.next
                carry_over += l1.val
            
            if l2.next is not None:
                l2 = l2.next
                carry_over += l2.val
                
            current_node.next = ListNode(carry_over % 10)
            carry_over //= 10
            current_node = current_node.next
            
    
        return ans_list
    
