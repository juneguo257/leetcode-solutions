# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        
        prev = None
        cur = head
        nextNode = head.next

        while (nextNode != None):
            # save this bc we overwrite it
            nextNode = cur.next

            # update it!
            cur.next = prev

            # continue iterating
            prev = cur
            cur = nextNode
        
        if (cur != None):
            return cur # singleton case
        return prev