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
    
  #reverse using Linked List
#remember that we need to reverse the linking, not data

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        curr=head
        while(curr is not None):
            nextTemp=curr.next
            curr.next=prev
            prev=curr
            curr=nextTemp
        return prev
            
        
            
            
        
