# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        fast=slow=head
        
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        tail, cur = None, slow.next
        slow.next = None
        
        while cur:
            cur.next, tail, cur = tail, cur, cur.next
            
       
        headCur, headNext = head, head.next
        tailCur, tailNext = tail, tail.next
        while True:
            headCur.next, tailCur.next = tailCur, headNext
             
            if not tailNext:
                return
            
            tailCur, headCur = tailNext, headNext
            tailNext, headNext = tailNext.next, headNext.next
