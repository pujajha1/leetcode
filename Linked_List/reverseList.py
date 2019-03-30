#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=[]
        l1=[]
        if head is None:
            return
        while head is not None:
            current=head.val
            l.append(current)
            head=head.next
        l1=l[::-1]
        
        current=dummy=ListNode(0)
        for e in l1:
            current.next=ListNode(e)
            current=current.next
        return dummy.next
            
        
            
            
        
