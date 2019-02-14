#https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
#    def __init__(self, x):
 #       self.val = x
  #      self.next = None
        


class Solution:
    
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':    
       #currl1=l1.val
        #currl2=l2.val
        s=""
        while l1!=None:
            s+=str(l1.val)
            l1=l1.next
        revs= int(s[::-1])    
        st=""
        while l2!=None:
            st+=str(l2.val)
            l2=l2.next
        revst=int(st[::-1])
        
        l= revs+revst
        k=[]
        for i in str(l):
            k.append(int(i))
        k1=k[::-1]
        return k1
