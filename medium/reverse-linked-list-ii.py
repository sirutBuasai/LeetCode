class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
      count = 1
      curr = head
      
      if left == right:
        return head
      
      else:
        while count < left:
          count += 1
          curr = curr.next 
        
        while count < right:
          swap = curr
          for _ in range(right-count):
            swap = swap.next
          curr.val, swap.val = swap.val, curr.val
          curr = curr.next
          count += 1
          right -= 1
              
      return head
      
