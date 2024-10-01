class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        if not fast.next:
            return slow
        else:
            return slow.next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        count = 0

        while head:
            count += 1
            head = head.next
            if count % 2 == 0:
                slow = slow.next

        return slow
