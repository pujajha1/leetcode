#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        a = int(str(x)[::-1])
        if x==a:
            return True
        return False
