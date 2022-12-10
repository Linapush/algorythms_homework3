# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# используем указатель slow and fast, если fast.next == slow.next, вернем True

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head

        while slow and fast: 
            fast = fast.next
            if fast == slow:
                return True
            elif not fast:
                return False
            slow = slow.next
            fast = fast.next
        else:
            return False