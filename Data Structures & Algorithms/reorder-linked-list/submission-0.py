# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        def reverseList(head):
            curr = head
            prev = None

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        first, second = head, reverseList(l2)
        
        while second:
            first_tmp = first.next
            second_tmp = second.next
            first.next = second
            second.next = first_tmp
            first = first_tmp
            second = second_tmp

        return
        