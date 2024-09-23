#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        if int(''.join(list(str(x))[::-1])) == x:
            return True
        return False

         # 2nd way
        strinh = str(x)
        length= len(strinh) - 1
        for i in range(0,len(strinh)):
            j = len(strinh)-(i+1)
            print(strinh[i], strinh[j])
            if strinh[i] != strinh[j] :
                return False
        return True

        # 3rd Way
        # strinh = str(x)
        # if strinh == strinh[::-1]:
        #     return True
        # return False
