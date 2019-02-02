#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x):
        a = int(str(abs(x))[::-1])
        if(a<pow(-2,31) or a>(pow(2,31)-1)):
            return 0
        if(x>0):
            return a
        return -abs(a)
