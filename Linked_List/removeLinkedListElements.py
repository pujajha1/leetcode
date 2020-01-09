#https://leetcode.com/problems/remove-linked-list-elements/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return
        if head.val==val and head.next is None:
            return 
        current_pointer=head
        next_pointer=current_pointer.next
        while(next_pointer is not None):
            if(next_pointer.val==val):
                current_pointer.next=next_pointer.next
                del next_pointer
                next_pointer=current_pointer.next
            else:
                current_pointer=next_pointer
                next_pointer=current_pointer.next
        if head.val==val:
            current_pointer=head
            head=head.next
            del current_pointer
