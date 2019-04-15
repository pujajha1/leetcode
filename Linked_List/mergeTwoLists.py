#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None:
            return None
        l3=ListNode
        current=l3
        while l1 and l2:
            if l1 is not None and l2 is not None:
                if(l1.val<=l2.val):
                    current.next=l1
                    l1=l1.next
                else:
                    current.next=l2
                    l2=l2.next
                current=current.next
        if l1:
            current.next=l1
        elif l2:
            current.next=l2
        return l3.next
                   
    

        
        
