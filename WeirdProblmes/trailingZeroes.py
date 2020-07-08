https://leetcode.com/problems/factorial-trailing-zeroes/submissions/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt=0
        while n!=0:
            n=n//5
            cnt+=n
        return cnt
