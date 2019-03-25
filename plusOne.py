#https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''.join(str(e) for e in digits)
        #str1='123'
        next=int(str1)+1
        #next=124
        k=list(map(int, str(next)))
        return k
        
