# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None or head.next == None):
            return False
        p1 = head.next
        p2 = head.next.next # must exist then

        # standard 2 ptr fast and slow ptr soln
        while (p1 != p2):
            if (p2 == None or p2.next == None): # p2 will always stumble upon end of list first
                return False
            p1 = p1.next
            p2 = p2.next.next # must exist
        return True