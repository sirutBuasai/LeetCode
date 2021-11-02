class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
          prev = curr
          curr = curr.next
          while curr and prev.val == curr.val:
            prev.next = curr.next
            curr = curr.next
            
        return head
        
