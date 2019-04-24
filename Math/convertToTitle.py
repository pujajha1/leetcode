#https://leetcode.com/problems/excel-sheet-column-title/submissions/
class Solution:
    def convertToTitle(self, n: int) -> str:
        chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res=""
        fi=len(chars)
        while n-1 >=0:
            res=chars[int((n-1)%fi)]+res
            n=(n-1)/fi
        return res
         
