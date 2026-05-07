# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = {}
        i = 0
        while head:
            if head in seen:
                return True
            else:
                seen[head] = i
            i += 1
            head = head.next
        return False

        