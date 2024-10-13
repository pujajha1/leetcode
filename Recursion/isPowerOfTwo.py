class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n%2 != 0:
            return False
        if pow(-2,31)>n or n>pow(2,31)-1:
            return False   
        else:
            return self.isPowerOfTwo(n//2)
        return False
