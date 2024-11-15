# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1, get length of linked list
        lLen = 0
        cur = head
        while (cur != None):
            cur = cur.next
            lLen += 1
        
        if (lLen == 1):
            return # singleton do not do anything
        
        # step 2: break linked list in half
        halfLen = lLen // 2
        secondHeadPrev = head

        curLen = 0
        while (curLen < (lLen - halfLen) - 1): # get node before nextHead
            secondHeadPrev = secondHeadPrev.next
            curLen += 1
        
        # step 2.5: reverse latter half
        prev = None
        cur = secondHeadPrev.next
        nextNode = cur.next
        while (nextNode != None):
            # get the next node in the original list
            nextNode = cur.next

            # prevent looping
            cur.next = prev

            # update previous ptrs
            prev = cur
            cur = nextNode

        secondHeadPrev.next = None

        if (prev == None): # singleton case (2 elements overall)
            prev = cur

        # step 3: re-merge the lists
        p1 = head
        p1Next = p1.next
        p2 = prev
        p2Next = p2.next

        # length of p2 can only be length of p1, or length of p1 + 1
        while (p1 != None and p2 != None):
            # save nexts before overwriting them
            p1Next = p1.next
            p2Next = p2.next

            # change structure
            p2.next = None
            p1.next = p2
            p2.next = p1Next

            # get the nexts back
            p1 = p1Next
            p2 = p2Next