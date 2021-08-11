class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
          return None
        
        list_len = 0
        curr_node = head

        while curr_node:
          list_len += 1
          curr_node = curr_node.next
          
        curr_node = head
        if list_len != n:
          for i in range(list_len-n):
            prev_node = curr_node
            curr_node = curr_node.next
            
          prev_node.next = curr_node.next

        else:
          curr_node = curr_node.next
          return curr_node

        return head
      
