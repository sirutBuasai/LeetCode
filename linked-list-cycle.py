class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        tortoise = head

        while hare is not None and hare.next is not None:
          hare = hare.next.next
          tortoise = tortoise.next
          
          if hare is tortoise:
            return True
          
        return False
      
