#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        if int(''.join(list(str(x))[::-1])) == x:
            return True
        return False
