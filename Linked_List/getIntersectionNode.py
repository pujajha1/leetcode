#https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return 
        slow=headA
        fast=headB
        while slow is not fast:
            if slow is None:
                slow=headB
            else:
                slow=slow.next
            if fast is None:
                fast=headA
            else:
                fast=fast.next
        return slow
