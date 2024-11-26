# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        # get p2 n + 1 ahead (so we can delete the real node)
        for i in range(n):
            if (p2.next == None): # only will happen if we wanted to delete head
                head = head.next
                return head
    
            p2 = p2.next
        
        # now, get p2 to the end, and progress p1 too
        while (p2.next != None):
            p1 = p1.next
            p2 = p2.next
        
        # remove node
        p1.next = (p1.next).next

        return head