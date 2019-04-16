#https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr=head
        prev=None
        if head is None:
            return
        
        if(curr.val==val):
            return self.removeElements(head.next,val)
        
        while curr.next is not None:
            prev=curr
            curr=curr.next
            if(curr.val==val):
                prev.next=curr.next
                curr=prev            
        return head
        
