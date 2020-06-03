#From Leetcode Solution:
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
      
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        current_pointer=head
        next_pointer=current_pointer.next
        
        while current_pointer.next is not None:
            if current_pointer.val==next_pointer.val:
                current_pointer.next=next_pointer.next
                del next_pointer
                next_pointer=current_pointer.next
                
            else:
                current_pointer=next_pointer
                next_pointer=current_pointer.next
        return head
 ####################################################################################################
#Second Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        prev=head
        some=prev.next
        while(some):
            if(prev.val==some.val):
                prev.next=some.next
                some=prev.next
            else:
                prev=prev.next
                some=prev.next
        return head
      
        
