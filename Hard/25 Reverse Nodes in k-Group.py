# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head
        
        l_list=[]
        # linked list -> list
        while head:
            l_list.append(head.val)
            head=head.next
       # reverse nodes in k-group     
        for i in range(0,len(l_list),k):
            if i+k>len(l_list):
                break
            tmp=l_list[i:i+k]
            tmp.reverse()
            l_list[i:i+k]=tmp
        # list-> linked list    
        node=new_head=ListNode()
        for val in l_list:
            node.next=ListNode(val,None)
            node=node.next
        
        return new_head.next
